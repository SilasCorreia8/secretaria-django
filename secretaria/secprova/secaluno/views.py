from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Aluno
from .forms import AlunoForm

# Create your views here.
def alunos(request):
    template = loader.get_template('myfirst.html')
    return HttpResponse(template.render())

def listar(request):
    buscarAlunos = Aluno.objects.all().values()
    template = loader.get_template('secaluno/listar.html')
    context = {
        'arrayAlunos': buscarAlunos,
    }
    return HttpResponse(template.render(context, request))

def addAluno(request):
    if request.method == "POST":
        form = AlunoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/secaluno/')
        
    else:
        form = AlunoForm()

    context = {
        'form': form
    }

    return render(request, 'secaluno/add.html', context)
    
    