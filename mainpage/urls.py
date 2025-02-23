from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'), # views.py should contain def index(request)..... 
    path('services/', views.services, name='services'), 
# добавить пути к остальным страницам
]