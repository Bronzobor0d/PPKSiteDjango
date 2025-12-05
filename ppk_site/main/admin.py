from django.contrib import admin
from .models import Specialty, Teacher, Chat, Message, News

# Register your models here.
admin.site.register(Specialty)
admin.site.register(Teacher)
admin.site.register(Chat)
admin.site.register(Message)
admin.site.register(News)