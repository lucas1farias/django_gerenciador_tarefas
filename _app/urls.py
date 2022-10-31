

# ae_2: Importar o configurador de rota
from django.urls import path

# ae_5: Importação da view do template inicial
from .views import IndexView

# ai_4: Importação da view de criação de conta
from .views import SignUpView

# aj_4: Importação da view que efetua login de conta
from .views import SignInView

# ak_3: Importação da view que efetua logout de conta
from .views import sign_out

# al_3: Importação da view que acessa as tarefas de uma conta de usuário
from .views import TasksListView

# am_2: Importação da view que cria as tarefas de uma conta de usuário
from .views import NewTaskCreateView

# ao_2: Importação da view que edita as tarefas de uma conta de usuário
from .views import AlterTaskUpdateView

# ap_2: Importação da view que remove as tarefas de uma conta de usuário
from .views import EraseTaskDeleteView

# ae_3: Criação desta var com a configuração da rota da primeira view
urlpatterns = [
    # ae_6: Criação da rota para a view inicial
    path('', IndexView.as_view(), name='index'),
    # ai_5: Criação da rota para a view que cria conta
    path('signup', SignUpView.as_view(), name='signup'),
    # aj_5: Criação da rota para a view que efetua login de uma conta de usuário
    path('signin', SignInView.as_view(), name='signin'),
    # ak_4: Criação da rota para a view que efetua o logout de uma conta de usuário
    path('signout', sign_out, name='signout'),
    # al_3: Criação da rota para a view que acessa tarefas de uma conta de usuário
    path('your-tasks', TasksListView.as_view(), name='your-tasks'),
    # am_2: Criação da rota para a view que criar as tarefas de uma conta de usuário
    path('create-task', NewTaskCreateView.as_view(), name='create-task'),
    # ROTAS QUE FAZEM USO DE LOOP DJANGO EM TEMPLATES USANDO VARS DE CONTEXTO CONFIGURADAS EM SUAS VIEWS
    # Atributo escolhido para identificar cada objeto: pk
    # ao_2: Criação da rota para a view que edita as tarefas de uma conta de usuário
    path('update-task/<int:pk>', AlterTaskUpdateView.as_view(), name='update-task'),
    # ap_2: Criação da rota para a view que remove as tarefas de uma conta de usuário
    path('erase-task/<int:pk>', EraseTaskDeleteView.as_view(), name='erase-task'),
]
