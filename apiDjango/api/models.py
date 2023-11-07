
from django.db import models




class Alumno(models.Model):
    idalumno = models.IntegerField( primary_key=True)  # AutoField en lugar de IntegerField
    nombre_alumno = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'alumno'



class Asignatura(models.Model):
    idasignatura = models.IntegerField(db_column='idAsignatura', primary_key=True)  # Field name made lowercase.
    nombre_asignatura = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'asignatura'


class DetalleAsistencia(models.Model):
    id_asis = models.AutoField(primary_key=True)
    alumno_idalumno = models.ForeignKey(Alumno, models.DO_NOTHING, db_column='Alumno_idAlumno')  # Field name made lowercase.
    profesor_idprofesor = models.ForeignKey('Profesor', models.DO_NOTHING, db_column='profesor_idprofesor')
    seccion_idseccion = models.ForeignKey('Seccion', models.DO_NOTHING, db_column='seccion_idseccion')
    fecha_asistida = models.DateField()
    cantidad_asistido = models.IntegerField()
    estado = models.CharField(max_length=45)
    porcentaje_asis = models.FloatField()

    class Meta:
        managed = False
        db_table = 'detalle_asistencia'


class Profesor(models.Model):
    idprofesor = models.IntegerField(primary_key=True)
    nombre_profesor = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'profesor'


class Seccion(models.Model):
    idseccion = models.IntegerField(primary_key=True)
    nombre_seccion = models.CharField(max_length=45)
    asignatura_idasignatura = models.ForeignKey(Asignatura, models.DO_NOTHING, db_column='Asignatura_idAsignatura')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'seccion'
