from django.shortcuts import render
from django.http import JsonResponse
import  json
from . import forms
from django.shortcuts import render, redirect
from .forms import ClientRegistrationForm
from django.contrib.auth import login
from django.contrib import messages

from .models import Work



def index(request):
    return render(request, 'mainpage/index.html')


def services(request):
    return render(request,'mainpage/services.html')

def about(request):
    return render(request, 'mainpage/about.html')

def projects(request):
    return render(request, 'mainpage/projects.html')

def contact(request):
    if request.method == "POST":
        form = forms.FeedBackForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': forms.FeedBackForm()}
    return render(request, 'mainpage/contact.html', context)

def workers(request):
    return render(
        request,
        'mainpage/workers.html'
    )

def worker_status(request):
    return JsonResponse({'Плиточник':'available', "Отделка":"unavailable"})


def work_types_api(request):
    works = Work.objects.all().values('id', 'name', 'cost_per_sqm')
    return JsonResponse(list(works), safe=False)


def register_client(request):
    if request.method == 'POST':
        form = ClientRegistrationForm(request.POST)
        if form.is_valid():

            client = form.save()
            login(request, client.user)
            messages.success(request, 'Регистрация прошла успешно!')
            return redirect('registration_success')
        else:
            messages.error(request, 'Пожалуйста, исправьте ошибки в форме.')
    else:
        form = ClientRegistrationForm()
    return render(request, 'mainpage/register.html', {'form': form})


def registration_success(request):
    return render(request, 'mainpage/registration_success.html')