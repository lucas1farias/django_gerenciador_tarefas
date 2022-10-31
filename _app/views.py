

# from django.shortcuts import render
# from django.core.validators import RegexValidator

# ae_4: Importação da "class based view"
from django.views.generic import TemplateView

# ai_2: Dependências para a configuração da class based view que cria uma conta de usuário
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import redirect

# aj_2: Para logar no usuário, além destas bibliotecas, também usa "redirect" e "messages", já chamados acima
from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth import login

# ak_1: Dependências usadas para deslogar um usuário logado
from django.contrib.auth import logout

# al_2: Dependências necessárias para a criação da view que registrará tarefas do usuário
from django.views.generic import ListView

# al_2: Modelo necessário para coletar os dados e exibí-los no template
from .models import Tasks

# am_1: Dependências necessárias para a criação de uma nova tarefa (se logado)
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView

# ao_1: Dependências necessárias para a edição de uma nova tarefa (se logado)
from django.views.generic import UpdateView

# ap_1: Dependências necessárias para a remoção de uma nova tarefa (se logado)
from django.views.generic import DeleteView


def ink_random(txt: str) -> str:
    from random import choice

    box: tuple = (
        '\033[1:30m', '\033[1:31m', '\033[1:32m', '\033[1:33m', '\033[1:34m', '\033[1:35m', '\033[1:36m',
        '\033[1:37m'
    )
    close_tag = '\033[1:38m'

    return f"{choice(box)}{txt}{close_tag}"


# ae_4: Primeira view (checando se há conta logada)
class IndexView(TemplateView):
    template_name = 'index.html'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # ag_1: A criação dessa var não é necessaria, mas foi feita para evitar muitos códigos em "get_context_data"
        self.context = None

    def show_user(self):
        return self.request.user

    # ag_2: Como verificar se uma conta está logada
    def user_exists(self):
        # self.request é INTEGRADO a qualquer "class based view" instanciada
        absent_user = self.request.user.is_anonymous

        if not absent_user:
            self.context['user'] = self.request.user.email

    def get_context_data(self, **kwargs):
        self.context = super(IndexView, self).get_context_data(**kwargs)
        # ag_3: Onde deve ser usada para não haver erro
        self.user_exists()
        self.context['user'] = self.show_user()
        return self.context


# ai_3: Configuração do backend para o template que cria uma conta de usuário
class SignUpView(TemplateView):
    template_name = 'sign-up.html'

    def post(self, request):
        msg = {
            'username_already_taken': 'O nome de usuário já existe.',
            'user_email_already_taken': 'Já há uma conta registrada com esse e-mail.',
            'passwords_do_not_match': 'Senha inicial e de confirmação, não são idênticas!',
            'sign-up-successful': '{account_} Seu cadastro foi realizado!'
        }

        conditions = {
            'passwords_are_!=': str(request.POST['password']) != str(request.POST['password_confirm']),
            'username_taken': User.objects.filter(username=request.POST['username']).exists(),
            'email_taken': User.objects.filter(email=request.POST['email']).exists()
        }

        # Se estiver enviando dados
        if str(request.method) == 'POST':
            # Se senhas são iguais
            if conditions['passwords_are_!=']:
                messages.error(request, msg['passwords_do_not_match'])
                return redirect('signup')
            # Se usuário já existe
            if conditions['username_taken']:
                messages.error(request, msg['username_already_taken'])
                return redirect('signup')
            # Se email já existe
            if conditions['email_taken']:
                messages.error(request, msg['user_email_already_taken'])
                return redirect('signup')

            # Se tudo estiver ok
            if True not in tuple(conditions.values()):
                new_user = User.objects.create_user(
                    first_name=request.POST['first_name'],
                    last_name=request.POST['last_name'],
                    username=request.POST['username'],
                    email=request.POST['email'],
                    password=request.POST['password']
                )
                new_user.save()
                messages.success(request, msg['sign-up-successful'].format(account_=new_user.get_full_name()))
                return redirect('index')


# aj_3: Configuração do backend para o template que loga numa conta de usuário
class SignInView(TemplateView):
    template_name = 'sign-in.html'

    def post(self, request):
        msg = {
            'logged_in': 'Login efetuado com sucesso!',
            'user_nonexistent': 'O usuário não existe!',
            'password_nonexistent': 'Senha incorreta!',
            'incorrect_data': 'Usuário ou senha incorretas'
        }

        if str(request.method) == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            "REMOVIDO (ignorado pelo Django)"
            # if not username:
            #     messages.error(request, msg['user_nonexistent'])
            #     return redirect('signin')
            # if not password:
            #     messages.error(request, msg['password_nonexistent'])
            #     return redirect('signin')

            ""
            # Retorna True ou None
            user = authenticate(request, username=username, password=password)

            if user:
                login(request, user)
                messages.success(request, msg['logged_in'])
                return redirect('index')
            if not user:
                messages.error(request, msg['incorrect_data'])
                return redirect('signin')


# ak_2: Configuração do backend para a ação que desloga uma conta de usuário logada
def sign_out(request):
    messages.success(request, 'Saída efetuada com sucesso')
    logout(request)
    return redirect('index')


# al_2: Configuração do backend para o template que exibe tarefas criadas por uma conta de usuário (se logada)
class TasksListView(ListView):
    # Nome da var de contexto, modelo exportado, por qual atributo ordenar, limite de item por página
    context_object_name = 'user_tasks'  # uso em: _app/templates/tasks-table.html
    model = Tasks
    ordering = 'created'                # não vêm de "Tasks", mas vêm de "Base", via herança
    paginate_by = 5                     # aq_2: só faz sentido, se há paginação Django sendo usada
    template_name = 'user-tasks.html'

    def get_context_data(self, **kwargs):
        context = super(TasksListView, self).get_context_data(**kwargs)
        # Var de contexto usada em: _app/templates/user-tasks.html
        context['tasks_database'] = Tasks.objects.all()
        context['user'] = self.request.user.email
        return context


# am_1: Configuração do backend para o template que cria uma tarefa de um usuário
class NewTaskCreateView(SuccessMessageMixin, CreateView):
    fields = ('task',)
    model = Tasks
    success_message = 'Uma nova tarefa foi adicionada!'
    success_url = reverse_lazy('your-tasks')
    template_name = 'create-task.html'


# ao_1: Configuração do backend para o template que edita uma tarefa de um usuário
class AlterTaskUpdateView(SuccessMessageMixin, UpdateView):
    fields = ('task',)
    model = Tasks
    success_message = 'Sua tarefa foi editada!'
    success_url = reverse_lazy('your-tasks')
    template_name = 'edit-task.html'


# ap_1: Configuração do backend para o template que remove uma tarefa de um usuário
class EraseTaskDeleteView(SuccessMessageMixin, DeleteView):
    model = Tasks
    success_message = 'A tarefa foi removida!'
    success_url = reverse_lazy('your-tasks')
    template_name = 'erase-task.html'


def handler404(request, exception):
    return render(request, '404.html')
