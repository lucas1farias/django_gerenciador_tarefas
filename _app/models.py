

from django.db import models


# al_1: Modelo base que pode ser aplicado a qualquer outro
class Base(models.Model):
    created = models.DateTimeField('Data de criação', auto_now_add=True)
    updated = models.DateTimeField('Última atualização', auto_now=True)
    availability = models.BooleanField('Disponibilidade', default=True)

    # Configurar para ser usado por qualquer outro modelo
    class Meta:
        abstract = True


# al_1: Modelo que cria tarefas de usuários
class Tasks(Base):
    task = models.CharField('Qual a tarefa a ser adicionada?', max_length=1500)

    def __str__(self):
        return self.task

    # Rótulos para o Django template admin
    class Meta:
        verbose_name = 'Tarefa'
        verbose_name_plural = 'Tarefas'
