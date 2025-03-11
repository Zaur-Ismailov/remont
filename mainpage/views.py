from django.shortcuts import render
from django.http import JsonResponse
import  json
from . import forms

def tasklist(request):
    return render(
        request,
        'mainpage/tasklist.html'
    )

def my_tasks(request):
    dela = {
        'утро':'покормить рыбок',
        'день': 'помыть пол',
        }

    if request.method == 'POST':
        print ('MY BODY', request.body)
        json_str = request.body.decode('utf-8')
        print(json_str)
        json_data = json.loads(json_str)
        print(json_data)
        return JsonResponse({
            json_data['когда']: dela[json_data['когда']]
        })
    
    return JsonResponse(dela)
        

def index(request):
    return render(
        request,
        'mainpage/index.html'
    )


def services(request):
    return render(
        request,
        'mainpage/services.html'
    )


def about(request):
    return render(
        request,
        'mainpage/about.html'
    )

def projects(request):
    return render(
        request,
        'mainpage/projects.html'
    )

def contact(request):
    if request.method == "POST":
        form = forms.FeedBackForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
    #else:
    context = {
        'form': forms.FeedBackForm(),
    }
    return render(
        request,                  # Запрос
	    'mainpage/contact.html',  # путь к шаблону
        context                   # подстановки
    )

def workers(request):
    return render(
        request,
        'mainpage/workers.html'
    )

def worker_status(request):
    return JsonResponse({'Плиточник':'available', "Отделка":"unavailable"})