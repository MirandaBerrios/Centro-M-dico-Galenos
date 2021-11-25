from django.db import models

class Paciente(models.Model):
    id_paciente = models.CharField(max_length=6 , null=True, verbose_name="Patente")
    rut_paciente = models.CharField(max_length=10, primary_key=True , blank=False, null=True, verbose_name="rut usuario")
    primer_nombre = models.CharField(max_length=50, null=False, blank=True, verbose_name="Primer nombre")
    segundo_nombre = models.CharField(max_length=50 , null=True, blank=True, verbose_name="Segundo nombre")
    apellido_paterno =models.CharField(max_length=50, null=False , blank=True, verbose_name="Apellido paterno")
    apellido_materno = models.CharField(max_length=50, null=False, blank=True , verbose_name="Apellido materno")
    fecha_nacimiento  = models.DateField()
    genero = models.CharField(max_length=1, verbose_name="Género")
    direccion = models.CharField(max_length=80, verbose_name="Dirección de residencia")
    email = models.CharField(max_length=40, verbose_name="Dirección de correo electrónico")
    telefono = models.CharField(max_length=12, verbose_name="Teléfono")
    contrasena = models.CharField(max_length=10, null=False, blank=False, verbose_name="Constraseña")
    contrasena2 = models.CharField(max_length=10, null=False, blank=False, verbose_name="Repetir contraseña")
    def __str__(self):
        return self.rut_paciente
