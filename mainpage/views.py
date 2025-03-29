from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from . import forms
from .models import WorkType, SelectedWork

def work_types_api(request):
    work_types = WorkType.objects.all().values('id', 'name', 'cost_per_sqm')
    return JsonResponse(list(work_types), safe=False)

def index(request):
    return render(request, 'mainpage/index.html')

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
    return render(request, 'mainpage/workers.html')

def worker_status(request):
    return JsonResponse({'Плиточник':'available', "Отделка":"unavailable"})

def services(request):
    if request.method == 'POST' and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        form = forms.SelectedWorkForm(request.POST)
        if form.is_valid():
            selected_work = form.save()
            return JsonResponse({
                'success': True,
                'work': {
                    'id': selected_work.id,
                    'name': selected_work.work_type.name,
                    'area': float(selected_work.area),
                    'cost': float(selected_work.total_cost),
                    'time': float(selected_work.total_time),
                }
            })
        else:
            return JsonResponse({'success': False, 'errors': form.errors}, status=400)
    
    form = forms.SelectedWorkForm()
    selected_works = SelectedWork.objects.all()
    total_cost = sum(work.total_cost for work in selected_works)
    total_time = sum(work.total_time for work in selected_works)
    
    context = {
        'form': form,
        'selected_works': selected_works,
        'total_cost': total_cost,
        'total_time': total_time,
    }
    return render(request, 'mainpage/services.html', context)

@csrf_exempt
def remove_work(request, work_id):
    if request.method in ['POST', 'DELETE']:
        try:
            work = SelectedWork.objects.get(id=work_id)
            work.delete()
            return JsonResponse({'success': True})
        except SelectedWork.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Work not found'}, status=404)
    return JsonResponse({'error': 'Invalid request'}, status=400)


def tasklist(request):
    return render(request, 'mainpage/tasklist.html')

