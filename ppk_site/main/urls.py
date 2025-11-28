from django.urls import path, include, re_path
from . import views
from django.conf.urls.static import static
from django.conf import settings

from django.views.static import serve

urlpatterns = [
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),

    path('', views.index, name='home'),
    path('specialities', views.specialities, name='specialities'),
    path('speciality/<int:pk>', views.SpecialtyDetailView.as_view(), name='specialty-detail'),
    path('teachers', views.teachers, name='teachers'),
    path('teacher/<int:pk>', views.TeacherDetailView.as_view(), name='teacher-detail')
]

