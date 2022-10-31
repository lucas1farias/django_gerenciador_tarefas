

"""
if
<a class="btn btn-primary" href="{% url 'create-task' %}">Adicionar tarefa</a>

else
<a class="btn btn-primary mb-4" href="{% url 'create-task' %}">Adicionar nova tarefa</a>
{% include 'tasks-table.html' %}
{% include 'pagination.html' %}

<td class="text-center">
<a class="btn btn-primary" href="{% url 'update-task' task.pk %}">editar</a>
<a class="btn btn-danger" href="{% url 'remove-task' task.pk %}">deletar</a>
</td>
"""
