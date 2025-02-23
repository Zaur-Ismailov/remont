from django.shortcuts import render

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

