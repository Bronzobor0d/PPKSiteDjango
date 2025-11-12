from django.shortcuts import render
from django.http import HttpResponse
from .models import Specialty


def index(request):
    specialities = Specialty.objects.all()
    return render(request, 'main/index.html', {'title': 'Главная страница', 'specialities': specialities})