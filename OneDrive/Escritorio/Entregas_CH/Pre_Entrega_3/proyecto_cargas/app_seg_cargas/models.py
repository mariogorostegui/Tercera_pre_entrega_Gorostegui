from django.db import models

# Create your models here.

class Usuarios(models.Model):
    nombre = models.CharField(max_length=64) 
    apellido = models.CharField(max_length=64)# Equivalente de str
    area = models.CharField(max_length=64)  # Equivalent de int
    
    def __str__(self):
        return f"{self.nombre} | {self.apellido} | {self.area}"

class Agentes(models.Model):
    nombre_fwr = models.CharField(max_length=64)  
    abrev_fwr = models.CharField(max_length=6) 
    ctc_fwr = models.TextField()
    
class Cargas(models.Model):
    mawb=models.CharField(max_length=12)
    hawb=models.CharField(max_length=12)
    incoterm = models.CharField(max_length=20)
    area = models.CharField(max_length=64)
    abrev_fwr = models.CharField(max_length=6)
    cotizacion = models.FloatField()
    bultos = models.IntegerField()
    peso = models.FloatField()
    volumen = models.FloatField()
    atd = models.DateField()
    ata = models.DateField()
    estado = models.CharField(max_length=12)
    retiro = models.DateField()