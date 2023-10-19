from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('about/', views.about),
    path('projects/', views.all_projects),
    path('project/<int:id>', views.get_project),
    path('tasks/', views.tasks)
]
