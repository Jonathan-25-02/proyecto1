from django.db import models

# Create your models here.
from django.db import models

# Empleado general
class Empleado(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_ingreso = models.DateField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

# Técnico de efectos especiales (subtipo de Empleado)
class Tecnico(models.Model):
    empleado = models.OneToOneField(Empleado, on_delete=models.CASCADE, primary_key=True)
    especialidad = models.CharField(max_length=100)

    def __str__(self):
        return f"Técnico: {self.empleado.nombre} {self.empleado.apellido} - {self.especialidad}"

# Productora de cine
class Productora(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=150)
    pais = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

# Creación (Elemento de atrezzo con efectos)
class Creacion(models.Model):
    id = models.AutoField(primary_key=True)
    descripcion = models.TextField()
    fecha_creacion = models.DateField()
    tecnico = models.ForeignKey(Tecnico, on_delete=models.CASCADE)
    productora = models.ForeignKey(Productora, on_delete=models.CASCADE)

    def __str__(self):
        return f"Creación {self.id} - {self.descripcion[:30]}"
