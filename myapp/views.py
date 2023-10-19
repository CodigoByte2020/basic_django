from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import render


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
    project = Project.objects.get(id=id)
    return HttpResponse(f'Proyecto: {project.name}')
