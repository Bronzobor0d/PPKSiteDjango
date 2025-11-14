from django.shortcuts import render
from django.http import HttpResponse
from .models import Specialty
from django.views.generic import DetailView


def index(request):
    specialities = Specialty.objects.all()[:3]
    return render(request, 'main/index.html', {'title': 'Главная страница', 'specialities': specialities})

def specialities(request):
    specialities = Specialty.objects.all()
    return render(request, 'main/specialties.html', {'title': 'Специальности', 'specialities': specialities})


class SpecialtyDetailView(DetailView):
    model = Specialty
    template_name = 'main/specialty_detail.html'
    context_object_name = 'specialty'