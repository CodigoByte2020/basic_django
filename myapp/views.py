from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateNewTask
import logging

_logger = logging.getLogger(__name__)


# Create your views here.
def index(request):
    # return HttpResponse('<h1>HELLO WORLD</h1>')
    context = {
        'name': 'Gianmarco',
        'projects': list(Project.objects.values())
    }
    return render(request=request, template_name='index.html', context=context)


def tasks(request):
    tasks = Task.objects.values()
    return render(request=request, template_name='task.html', context={
        'tasks': tasks
    })


def about(request):
    # return HttpResponse('<h3>ABOUT</h3>')
    return render(request, 'about.html')


def all_projects(request):
    projects = list(Project.objects.values())
    return JsonResponse(projects, safe=False)


def get_project(request, id):
    # project = Project.objects.get(id=id)
    project = get_object_or_404(Project, id=id)
    # return HttpResponse(f'Proyecto: {project.name}')
    tasks = Task.objects.filter(project_id=id)
    return render(request=request, template_name='project_task.html', context={
        'project': project,
        'tasks': tasks
    })

def create_task(request):
    # _logger.info(f'******* REQUEST ******** {request.GET.get("title", "")} - {request.GET.get("description", "")}')
    # print(f'******* REQUEST ******** {request.GET.get("title", "")} - {request.GET.get("description", "")}')
    if request.method == 'GET': # SE OBTIENEN RECURSOS CON EL MÉTODO GET
        return render(request=request, template_name='create_task.html', context={
            'form': CreateNewTask()
        })
    elif request.method == 'POST': # SE CREAN RECURSOS CON EL MÉTODO POST
        Task.objects.create(title=request.POST['title'], description=request.POST['description'], project_id=1)
        # return redirect('/tasks')
        return redirect('tareas')  # PATH OR PATH NAME

def detail_task(request, id):
    print(id)
    task = Task.objects.get(id=id)
    return render(request=request, template_name='task_detail.html', context={'task': task})
