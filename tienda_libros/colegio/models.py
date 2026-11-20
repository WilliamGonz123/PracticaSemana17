from django.db import models


class Carrera(models.Model):
    nombre = models.CharField(max_length=100)
    anos = models.IntegerField()
    activa = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre


class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()
    edad = models.IntegerField()
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class Nota(models.Model):
    materia = models.CharField(max_length=100)
    valor = models.FloatField()
    aprobado = models.BooleanField(default=True)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.materia} ({self.valor})"