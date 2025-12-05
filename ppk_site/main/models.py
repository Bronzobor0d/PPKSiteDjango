from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


class Specialty(models.Model):
    title = models.CharField('Название', max_length=100)
    code = models.CharField('Код', max_length=20)
    qualification = models.CharField('Квалификация', max_length=100)
    description = models.TextField('Описание')
    form_of_education = models.CharField('Форма обучения', max_length=20)
    education_level = models.CharField('Уровень образования', max_length=20)
    period_of_study = models.CharField('Срок обучения', max_length=20)
    image_main = models.ImageField('Главная картинка', blank=True, null=True, upload_to='images')
    image_description = models.ImageField('Картинка в описании', blank=True, null=True, upload_to='images')
    lastedit_date = models.DateTimeField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Специальность'
        verbose_name_plural = 'Специальности'


class Teacher(models.Model):
    second_name = models.CharField('Фамилия', max_length=50)
    first_name = models.CharField('Имя', max_length=50)
    patronymic = models.CharField('Отчество', max_length=50)
    position = models.CharField('Должность', max_length=100)
    teaching_experience = models.IntegerField('Педагогический стаж')
    qualification_category = models.CharField('Квалификационная категория', max_length=100)
    professional_education = models.TextField('Профессиональное  образование')
    professional_development = models.TextField('Сведения о повышении квалификации')
    awards_and_achievements = models.TextField('Награды и достижения')
    subjects_and_modules_taught = models.TextField('Преподаваемые дисциплины и модули')
    lastedit_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.second_name + ' ' + self.first_name + ' ' + self.patronymic

    class Meta:
        verbose_name = 'Преподаватель'
        verbose_name_plural = 'Преподаватели'


class Chat(models.Model):
    user_owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_owner', verbose_name='Владелец')
    user_participant= models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_participant',verbose_name='Участник')
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Чат ' + self.user_owner.username + ' и ' + self.user_participant.username

    class Meta:
        verbose_name = 'Чат'
        verbose_name_plural = 'Чаты'


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, verbose_name='Чат')
    message = models.TextField('Сообщение')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'


class News(models.Model):
    title = models.CharField('Заголовок', max_length=100)
    text = models.TextField('Текст')
    image = models.ImageField('Картинка', blank=True, null=True, upload_to='images')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'