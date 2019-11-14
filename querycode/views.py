from django.shortcuts import render


from .models import AuCode


def index(request):
    return render(request, 'querycode/index.html')


def detail(request):
    return render(request, 'querycode/detail.html')
