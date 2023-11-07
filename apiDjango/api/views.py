from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Alumno , Profesor , Asignatura , Seccion , DetalleAsistencia
from .serializers import AlumnoSerializers , ProfesorSerializers,AsignaturaSerializers,SeccionSerializers,Detalle_asistenciaSerializers
from rest_framework import generics
from django.http import HttpResponse
from rest_framework.views import APIView

# Create your views here.

class AlumnoLista(generics.ListCreateAPIView):
    queryset=Alumno.objects.all()
    serializer_class = AlumnoSerializers

class AlumnoDelete(generics.DestroyAPIView):
    queryset = Alumno.objects.all()  
    serializer_class = AlumnoSerializers  
    
# -------------------------------------------------------------    
class ProfesorLista(generics.ListCreateAPIView):
    queryset=Profesor.objects.all()
    serializer_class = ProfesorSerializers
    
class ProfesorDelete(generics.DestroyAPIView):
    queryset=Profesor.objects.all()
    serializer_class = ProfesorSerializers

# -------------------------------------------------------------

class AsignaturaLista(generics.ListCreateAPIView):
    queryset=Asignatura.objects.all()
    serializer_class = AsignaturaSerializers
    
class AsignaturaDelete(generics.ListCreateAPIView):
    queryset=Asignatura.objects.all()
    serializer_class = AsignaturaSerializers
# -------------------------------------------------------------
    
class SeccionLista(generics.ListCreateAPIView):
    queryset=Seccion.objects.all()
    serializer_class = SeccionSerializers

class SeccionDelete(generics.DestroyAPIView):
    queryset=Seccion.objects.all()
    serializer_class = SeccionSerializers

# -------------------------------------------------------------

class Detalle_asistenciaLista(generics.ListCreateAPIView):
    queryset=DetalleAsistencia.objects.all()
    serializer_class = Detalle_asistenciaSerializers
    
class Detalle_asistenciaDelete(generics.DestroyAPIView):
    queryset=DetalleAsistencia.objects.all()
    serializer_class = Detalle_asistenciaSerializers




# class 


class RootView(APIView):
    def get(self, request):
        return HttpResponse("¡Que pasa larva!")
