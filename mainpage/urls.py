from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'), # views.py should contain def index(request)..... 
    path('services/', views.services, name='services'), 
    path('projects/', views.projects, name='projects'), 
    path('about/', views.about, name='about'), 
    path('contact/', views.contact, name='contact'),
    path('tasklist/', views.tasklist, name='tasklist'),
    path('my_tasks/', views.my_tasks, name='my_tasks'),
    path('workers/', views.workers, name='workers'),
    path('worker_status/', views.worker_status, name='worker_status'),

    

# добавить пути к остальным страницам
]