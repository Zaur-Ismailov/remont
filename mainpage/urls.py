from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'), # views.py should contain def index(request)..... 
    path('services/', views.services, name='services'), 
    path('projects/', views.projects, name='projects'), 
    path('about/', views.about, name='about'), 
    path('contact/', views.contact, name='contact')

# добавить пути к остальным страницам
]