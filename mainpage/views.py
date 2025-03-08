from django.shortcuts import render
from . import forms

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