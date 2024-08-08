from django.db import models

from django.db import models

class Profesionales(models.Model):
    IdProfesional = models.AutoField(primary_key=True)
    NroRegistro = models.CharField(max_length=50)
    Sexo = models.CharField(max_length=10)
    Nombres = models.CharField(max_length=100)
    ApellidoPaterno = models.CharField(max_length=50)
    ApellidoMaterno = models.CharField(max_length=50)
    FechaNacimiento = models.DateField()
    FechaRegistro = models.DateField()
    Nacionalidad = models.CharField(max_length=50)
    Rut = models.IntegerField()
    Dv = models.CharField(max_length=1)
    CodigoBusqueda = models.CharField(max_length=100)
    Universidad = models.CharField(max_length=100)
    Observaciones = models.TextField(blank=True, null=True)
    FechaCarga = models.DateField()

    class Meta:
        db_table = 'Profesionales'

class Antecedentes(models.Model):
    IdAntecedente = models.AutoField(primary_key=True)
    IdProfesional = models.ForeignKey(Profesionales, on_delete=models.CASCADE, related_name='antecedentes', db_column='IdProfesional')
    ClaseAntecedente = models.CharField(max_length=50)
    CodAntecedente = models.CharField(max_length=100)
    FechaAntecedente = models.DateField()
    FechaRegistro = models.DateField()
    NroResolucion = models.CharField(max_length=50)
    Procedencia = models.CharField(max_length=100)
    TipoAntecedente = models.CharField(max_length=1)

    class Meta:
        db_table = 'Antecedentes'
