from django.shortcuts import render
from django.http import JsonResponse
import  json
from . import forms
from django.shortcuts import render, redirect
from .forms import ClientRegistrationForm
from django.contrib.auth import login
from django.contrib import messages
from .models import Work
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ProjectForm, ProjectWorkForm
from .models import Work, Project, ProjectWork
from decimal import Decimal



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


@login_required
def create_project(request):
    try:
        client = request.user.client
    except Client.DoesNotExist:
        messages.error(request, 'Ваш аккаунт не связан с клиентом')
        return redirect('home')

    if request.method == 'POST':
        project_form = ProjectForm(request.POST)
        work_form = ProjectWorkForm(request.POST)

        if project_form.is_valid():
            project = project_form.save(commit=False)
            project.user = request.user
            project.client = client
            project.status = 'В обработке'
            project.save()

            works = Work.objects.all()
            total_cost = Decimal('0.00')

            for work in works:
                volume_str = request.POST.get(f'work_{work.id}_volume', '0')
                multiplier_str = request.POST.get(f'work_{work.id}_multiplier', '1')

                try:
                    volume = Decimal(volume_str) if volume_str else Decimal('0')
                    multiplier = Decimal(multiplier_str) if multiplier_str else Decimal('1')

                    if volume > Decimal('0'):
                        work_cost = volume * work.cost_per_sqm * multiplier
                        total_cost += work_cost

                        ProjectWork.objects.create(
                            project=project,
                            work=work,
                            volume=volume,
                            multiplier=int(multiplier),
                            details="Автоматически создано при создании проекта"
                        )

                except (ValueError, TypeError) as e:
                    messages.error(request, f"Ошибка в данных для работы '{work.name}': {str(e)}")
                    continue


            project.save()

            messages.success(request, 'Проект успешно создан!')
            return redirect('projects')

    else:
        project_form = ProjectForm()
        work_form = ProjectWorkForm()

    return render(request, 'mainpage/create_project.html', {
        'project_form': project_form,
        'work_form': work_form,
        'works': Work.objects.all()
    })