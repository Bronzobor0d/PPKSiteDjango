import random

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Specialty, Teacher, Chat, Message
from django.db.models import Q
from django.views.generic import DetailView
from django.shortcuts import redirect
from django.conf import settings
from .forms import SignUpForm, LoginForm, ChatCreateForm, MessageCreateForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib import messages


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
    return render(request, 'main/index.html',
                  {'title': 'Главная страница', 'specialities': specialities, 'teachers': teachers,
                   'banners': ['1', '2', '3']})


def specialities(request):
    specialities = Specialty.objects.all()

    return render(request, 'main/specialties.html',
                  {'title': 'Специальности', 'specialities': specialities, 'banners': ['1', '2', '3']})


def teachers(request):
    teachers = Teacher.objects.all()
    return render(request, 'main/teachers.html',
                  {'title': 'Преподаватели', 'teachers': teachers, 'banners': ['1', '2', '3']})


def sitemap(request):
    teachers = Teacher.objects.all()
    specialities = Specialty.objects.all()
    return render(request, 'main/sitemap.html',
                  {'title': 'Карта сайта', 'specialities': specialities, 'teachers': teachers})


@login_required
def chats(request):
    if request.user.is_staff:
        users = User.objects.exclude(Q(id=request.user.id))
    else:
        users = User.objects.exclude(Q(id=request.user.id) | Q(is_staff=False))

    user_forms = []
    for user in users:
        chat_exists = Chat.objects.filter(
            user_owner=request.user,
            user_participant=user
        ).exists() or Chat.objects.filter(
            user_owner=user,
            user_participant=request.user
        ).exists()

        user_chat = 0
        if chat_exists:
            user_chat = Chat.objects.filter(
                Q(user_owner=user, user_participant=request.user) | Q(user_owner=request.user,
                                                                      user_participant=user)).first()

        user_forms.append({
            'user': user,
            'form': ChatCreateForm(initial={'user_owner_id': user.id}),
            'chat_exists': chat_exists,
            'user_chat': user_chat
        })

    context = {
        'title': 'Тех-поддержка',
        'user_forms': user_forms,
        'banners': ['1', '2', '3']
    }

    return render(request, 'main/chats.html', context)


@login_required
def create_chat(request):
    if request.method == 'POST':
        form = ChatCreateForm(request.POST)
        if form.is_valid():
            user_owner_id = form.cleaned_data['user_owner_id']
            try:
                user_owner = get_object_or_404(User, id=user_owner_id)

                if Chat.objects.filter(user_owner=user_owner,
                                       user_participant=request.user).exists() or Chat.objects.filter(
                        user_owner=request.user, user_participant=user_owner).exists():
                    messages.warning(request, 'Чат с этим пользователем уже существует')
                else:
                    chat = Chat.objects.create(
                        user_owner=user_owner,
                        user_participant=request.user
                    )
                    messages.success(request, f'Чат с {user_owner.username} создан')

                    return redirect('chat-detail', pk=chat.pk)

            except IntegrityError:
                messages.error(request, 'Ошибка при создании чата')
            except User.DoesNotExist:
                messages.error(request, 'Пользователь не найден')

    return redirect('chats')


@login_required
def create_message(request):
    if request.method == 'POST':
        form = MessageCreateForm(request.POST)
        if form.is_valid():
            Message.objects.create(
                user=request.user,
                chat_id=form.cleaned_data['chat_id'],
                message=form.cleaned_data['message'])
            return redirect('chat-detail', pk=form.cleaned_data['chat_id'])

    return redirect('chats')


class SpecialtyDetailView(DetailView):
    model = Specialty
    template_name = 'main/specialty_detail.html'
    context_object_name = 'specialty'
    extra_context = {'title': 'Карта сайта', 'specialities': Specialty.objects.all(), 'banners': ['1', '2', '3']}


class TeacherDetailView(DetailView):
    model = Teacher
    template_name = 'main/teacher_detail.html'
    context_object_name = 'teacher'
    extra_context = {'teachers': Teacher.objects.all(), 'banners': ['1', '2', '3']}


class ChatDetailView(DetailView):
    model = Chat
    template_name = 'main/chat_detail.html'
    context_object_name = 'chat'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['messages'] = Message.objects.filter(chat=self.object)
        context['banners'] = ['1', '2', '3']
        context['form'] = MessageCreateForm()
        return context
