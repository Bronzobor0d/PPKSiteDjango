from django.urls import path, include, re_path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.sitemaps.views import sitemap
from .sitemap import SpecialtySitemap
from .sitemap import TeacherSitemap

from django.views.static import serve

sitemaps = {'specialty': SpecialtySitemap, 'teacher': TeacherSitemap}

urlpatterns = [
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),

    path('', views.index, name='home'),
    path('specialities', views.specialities, name='specialities'),
    path('speciality/<int:pk>', views.SpecialtyDetailView.as_view(), name='specialty-detail'),
    path('teachers', views.teachers, name='teachers'),
    path('teacher/<int:pk>', views.TeacherDetailView.as_view(), name='teacher-detail'),
    path('sitemap', views.sitemap, name='sitemap'),

    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),

    path('set-theme/', views.set_theme, name='set_theme'),

    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    path('chats/', views.chats, name='chats'),
]
