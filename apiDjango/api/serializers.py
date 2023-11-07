from .models import Alumno,Profesor,Asignatura,Seccion,DetalleAsistencia
from rest_framework import serializers


class AlumnoSerializers(serializers.ModelSerializer):
    class Meta:
        model=Alumno
        fields = "__all__"

class ProfesorSerializers(serializers.ModelSerializer):
    class Meta:
        model=Profesor
        fields = "__all__"
class AsignaturaSerializers(serializers.ModelSerializer):
    class Meta:
        model=Asignatura
        fields = "__all__"
class SeccionSerializers(serializers.ModelSerializer):
    class Meta:
        model=Seccion
        fields = "__all__"        
class Detalle_asistenciaSerializers(serializers.ModelSerializer):
    class Meta:
        model=DetalleAsistencia
        fields = "__all__"  