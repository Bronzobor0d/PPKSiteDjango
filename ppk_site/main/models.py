from django.db import models

# Create your models here.
class Specialty(models.Model):
    title = models.CharField('Название', max_length=100)
    code = models.CharField('Код', max_length=20)
    qualification = models.CharField('Квалификация', max_length=100)
    description = models.TextField('Описание')
    form_of_education = models.CharField('Форма обучения', max_length=20)
    education_level = models.CharField('Уровень образования', max_length=20)
    period_of_study = models.CharField('Срок обучения', max_length=20)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Специальность'
        verbose_name_plural = 'Специальности'