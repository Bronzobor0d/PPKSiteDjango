import random

from django.shortcuts import render
from django.http import HttpResponse
from .models import Specialty, Teacher, Chat
from django.db.models import Q
from django.views.generic import DetailView
from django.shortcuts import redirect
from django.conf import settings
from .forms import SignUpForm, LoginForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User


def set_theme(request):
    if request.method == 'POST':
        theme = request.POST.get('theme', settings.DEFAULT_THEME)

        if theme in settings.THEMES:
            request.session['theme'] = theme
            request.session.modified = True

    referer = request.META.get('HTTP_REFERER', '/')
    return redirect(referer)


def page_not_found(request, exception):
    return render(request, 'main/404.html', status=404)


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'main/signup.html', {'form': form})


def login_view(request):
    form = LoginForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    return render(request, 'main/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')


def index(request):
    specialities = Specialty.objects.all()[:3]
    teachers = Teacher.objects.all()[:3]
    return render(request, 'main/index.html', {'title': 'Главная страница', 'specialities': specialities, 'teachers': teachers, 'banners': ['1','2','3']})


def specialities(request):
    specialities = Specialty.objects.all()

    return render(request, 'main/specialties.html', {'title': 'Специальности', 'specialities': specialities, 'banners': ['1','2','3']})


def teachers(request):
    teachers = Teacher.objects.all()
    return render(request, 'main/teachers.html', {'title': 'Преподаватели', 'teachers': teachers, 'banners': ['1','2','3']})


def sitemap(request):
    teachers = Teacher.objects.all()
    specialities = Specialty.objects.all()
    return render(request, 'main/sitemap.html', {'title': 'Карта сайта', 'specialities': specialities, 'teachers': teachers})


def chats(request):
    users = User.objects.filter(is_staff=True)
    chats = Chat.objects.filter(
        Q(user_owner=request.user) |
        Q(user_participant=request.user))

    return render(request, 'main/chats.html', {'title': 'Преподаватели', 'users': users, 'banners': ['1','2','3']})


class SpecialtyDetailView(DetailView):
    model = Specialty
    template_name = 'main/specialty_detail.html'
    context_object_name = 'specialty'
    extra_context = {'specialities': Specialty.objects.all(), 'banners': ['1','2','3']}

class TeacherDetailView(DetailView):
    model = Teacher
    template_name = 'main/teacher_detail.html'
    context_object_name = 'teacher'
    extra_context = {'teachers': Teacher.objects.all(), 'banners': ['1','2','3']}

class ChatDetailView(DetailView):
    model = User
    template_name = 'main/teacher_detail.html'
    context_object_name = 'teacher'
    extra_context = {'teachers': Teacher.objects.all(), 'banners': ['1','2','3']}