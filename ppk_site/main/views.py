from django.shortcuts import render
from django.http import HttpResponse
from .models import Specialty, Teacher
from django.views.generic import DetailView


def page_not_found(request, exception):
    return render(request, 'main/404.html', status=404)


def index(request):
    specialities = Specialty.objects.all()[:3]
    teachers = Teacher.objects.all()[:3]
    return render(request, 'main/index.html', {'title': 'Главная страница', 'specialities': specialities, 'teachers': teachers})

def specialities(request):
    specialities = Specialty.objects.all()
    return render(request, 'main/specialties.html', {'title': 'Специальности', 'specialities': specialities})

def teachers(request):
    teachers = Teacher.objects.all()
    return render(request, 'main/teachers.html', {'title': 'Преподаватели', 'teachers': teachers})

class SpecialtyDetailView(DetailView):
    model = Specialty
    template_name = 'main/specialty_detail.html'
    context_object_name = 'specialty'
    extra_context = {'specialities': Specialty.objects.all()}

class TeacherDetailView(DetailView):
    model = Teacher
    template_name = 'main/teacher_detail.html'
    context_object_name = 'teacher'
    extra_context = {'teachers': Teacher.objects.all()}