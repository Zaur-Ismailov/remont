from django.urls import path
from . import views
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView # Импортируем LoginView и LogoutView

urlpatterns = [
    path('', views.index, name='home'),
    path('services/', views.services, name='services'), 
    path('projects/', views.projects, name='projects'), 
    path('about/', views.about, name='about'), 
    path('contact/', views.contact, name='contact'),
    path('workers/', views.workers, name='workers'),
    path('worker_status/', views.worker_status, name='worker_status'),
    path('api/work_types/', views.work_types_api, name='work_types_api'),
    path('register/', views.register_client, name='register_client'),
    path('register/success/', views.registration_success, name='registration_success'),
    path('login/', LoginView.as_view(next_page='home', template_name='mainpage/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout')
]