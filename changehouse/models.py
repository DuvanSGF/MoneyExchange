from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
TIPOPER = (
       ('0', 'Natural'),
       ('1', 'Juridica'),
)

ESTADOS = (('0', 'Activo'), ('1', 'Desactivo'))

TIPOID = (
       ('0', 'TI'),
       ('1', 'CC'),
       ('2', 'PA')
)

CHANGE = (('0', 'Dolares a Pesos'), ('Pesos a Dolares'))

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
    Cli_Nombre = models.CharField(max_length=25)
    Cli_Apellido = models.CharField(max_length=25)
    Cli_TipoID = models.CharField(max_length=1, choices=TIPOID, default="0")
    Cli_Identificacion = models.IntegerField()
    Cli_Direccion = models.CharField(max_length=50)
    Cli_Telefono = models.CharField(max_length=50)
    Cli_Persona = models.CharField(max_length=1, choices=TIPOPER, default="0", help_text='Tipo de persona')
    Cli_Estado = models.CharField(max_length=1, choices=ESTADmoOS, default="0")
    Cli_User_ID = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

class VentaCompra(models.Model):
    id_venta = models.AutoField(primary_key=True)
    Ven_Created = models.DateTimeField(default=timezone.now)
    Ven_Cliente_ID = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    Ven_Precio = models.CharField(max_length=50)
    Ven_Cantidad = models.CharField(max_length=50)
    Ven_Total = models.CharField(max_length=50)
