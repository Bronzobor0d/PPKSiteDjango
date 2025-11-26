from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name='home'),
    path('specialities', views.specialities, name='specialities'),
    path('speciality/<int:pk>', views.SpecialtyDetailView.as_view(), name='specialty-detail'),
    path('teachers', views.teachers, name='teachers'),
    path('teacher/<int:pk>', views.TeacherDetailView.as_view(), name='teacher-detail')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
