from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

# Create your models here.

TIPOPER = (
       ('Natural', 'N'),
       ('Juridica', 'J'),
)

ESTADOS = (('0', 'Activo'), ('1', 'Desactivo'))

TIPOID = (
       ('TI', 'TI'),
       ('CC', 'CC'),
)

CHANGE = (('0', 'Dolares a Pesos'), ('1','Pesos a Dolares'))

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tipoid = models.CharField(max_length=1, choices=TIPOID, default="1")
    identificacion = models.IntegerField()
    description = models.CharField(max_length=100, default='')
    city = models.CharField(max_length=100, default='')
    website = models.URLField(default=0)
    phone = models.IntegerField(default=0)
    image = models.ImageField(upload_to='profile_image', blank=True, default="profile_image/zx.jpg")

    def __str__(self):
        return self.user.username


class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    Cli_Nombre = models.CharField("Nombres", max_length=25)
    Cli_Apellido = models.CharField(max_length=25)
    Cli_TipoID = models.CharField(max_length=2, choices=TIPOID, default="TI")
    Cli_Identificacion = models.IntegerField()
    Cli_Direccion = models.CharField(max_length=50)
    Cli_Telefono = models.CharField(max_length=50)
    Cli_Persona = models.CharField(max_length=10, choices=TIPOPER, default="Natural")
    Cli_Estado = models.CharField(max_length=1, choices=ESTADOS, default="0")
    Cli_User_ID = models.ForeignKey(UserProfile, on_delete=models.CASCADE)


    def __str__(self):
        return self.Cli_Persona

class Compra(models.Model):
    id_compra = models.AutoField(primary_key=True)
    com_tipo = models.CharField(max_length=2, choices=CHANGE, default="0")
    Com_Created = models.DateTimeField(default=timezone.now)
    Com_Cliente_ID = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    Com_Precio = models.CharField(max_length=50)
    Com_Cantidad = models.CharField(max_length=50)

    def __str__(self):
        return self.Com_Precio
