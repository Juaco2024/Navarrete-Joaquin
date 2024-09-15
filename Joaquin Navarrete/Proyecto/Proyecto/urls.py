from django.contrib import admin
from django.urls import path
from productos_App.views import index, instructores, cursos, egresados

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('instructores/', instructores, name='instructores'),
    path('cursos/', cursos, name='cursos'),
    path('egresados/', egresados, name='egresados'),
]