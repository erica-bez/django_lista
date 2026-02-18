from django.shortcuts import render
from .models import tarefa

# Create your views here.
def lista_tarefas(request):
    tarefas = tarefa.objects.all()
    return render(request, 'lista/lista.html', {'tarefas': tarefas})