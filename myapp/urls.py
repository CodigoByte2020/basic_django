from django.urls import path
from . import views

# URL NAMES: PARA PODER REFERENCIAR EL PATH USANDO SU NAME, ESTO ES PARA NO CAMBIAR EL PATH EN TODOS LOS SITIOS.

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('projects/', views.all_projects, name='projects'),
    path('project/<int:id>', views.get_project, name='project_detail'),
    path('tasks/', views.tasks, name='tareas'),  # NAME: PATH NAME
    path('create_task/', views.create_task, name='create_task'),  # FILE PATH, FUNCTION
    path('task_detail/<int:id>', views.detail_task, name='task_detail')
]
