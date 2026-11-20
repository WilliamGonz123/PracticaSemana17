from django.urls import path
from . import views

urlpatterns = [
    path('', views.ver_carreras, name='inicio'),

    path('carreras/', views.ver_carreras, name='ver_carreras'),
    path('carreras/crear/', views.crear_carrera, name='crear_carrera'),
    path('carreras/editar/<int:id>/', views.editar_carrera, name='editar_carrera'),
    path('carreras/borrar/<int:id>/', views.borrar_carrera, name='borrar_carrera'),

    path('estudiantes/', views.ver_estudiantes, name='ver_estudiantes'),
    path('estudiantes/crear/', views.crear_estudiante, name='crear_estudiante'),
    path('estudiantes/editar/<int:id>/', views.editar_estudiante, name='editar_estudiante'),
    path('estudiantes/borrar/<int:id>/', views.borrar_estudiante, name='borrar_estudiante'),

    path('notas/', views.ver_notas, name='ver_notas'),
    path('notas/crear/', views.crear_nota, name='crear_nota'),
    path('notas/editar/<int:id>/', views.editar_nota, name='editar_nota'),
    path('notas/borrar/<int:id>/', views.borrar_nota, name='borrar_nota'),
]