from rest_framework import urlpatterns
from django.urls import re_path as url
from api import views
from django.urls import path
from rest_framework.views import APIView 
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.RootView.as_view(), name='root'),  
    
    
    path('api/alumno/', views.AlumnoLista.as_view()),
    path('api/alumno/<int:pk>/', views.AlumnoDelete.as_view(), name='alumno-delete'),
    
    path('api/profesor',views.ProfesorLista.as_view()),
    path('api/profesor/<int:pk>/', views.ProfesorDelete.as_view(), name='profesor-delete'),
    
    path('api/asignatura',views.AsignaturaLista.as_view()),
    path('api/asignatura/<int:pk>/', views.ProfesorDelete.as_view(), name='asignatura-delete'),
    
    path('api/seccion',views.SeccionLista.as_view()),
    path('api/seccion/<int:pk>/', views.SeccionDelete.as_view(), name='seccion-delete'),
    
    path('api/detalle-asistencia',views.Detalle_asistenciaLista.as_view()),
    path('api/detalle-asistencia/<int:pk>/', views.Detalle_asistenciaDelete.as_view(), name='dta-delete'),
    

    
]

urlpatterns = format_suffix_patterns(urlpatterns)
