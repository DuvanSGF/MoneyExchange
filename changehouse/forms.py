from django import forms
from changehouse.models import Cliente, Compra
from django.forms.utils import flatatt
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from changehouse.models import UserProfile

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = [
            'Cli_Nombre',
            'Cli_Apellido',
            'Cli_TipoID',
            'Cli_Identificacion',
            'Cli_Direccion',
            'Cli_Telefono',
            'Cli_Persona',
            'Cli_User_ID',
        ]

        labels = {
            'Cli_Apellido': 'Apellidos',
            'Cli_TipoID': 'Tipo de identificacion',
            'Cli_Identificacion': 'Numero de identificacion',
            'Cli_Direccion': 'Direccion',
            'Cli_Telefono': 'Telefono',
            'Cli_Persona': 'Tipo persona',
            'Cli_User_ID': 'Cambista',
        }

    widgets  =  {

                'Cli_Nombre': forms.TextInput(attrs={'class':'form-control'}),
                'Cli_Apellido': forms.TextInput(attrs={'class':'form-control'}),
                'Cli_TipoID': forms.Select(attrs={'class':'form-control'}),
                'Cli_Identificacion': forms.NumberInput(attrs={'class':'form-control'}),
    	        'Cli_Direccion': forms.NumberInput(attrs={'class':'form-control'}),
    	        'Cli_Telefono': forms.NumberInput(attrs={'class':'form-control'}),
                'Cli_Persona': forms.Select(attrs={'class':'form-control'}),
                'Cli_User_ID': forms.Select(attrs={'class':'form-control'}),

        }

def clean(self, *arg, **kwargs):
    cleaned_data = super(ClienteForm, self).clean(*arg, **kwargs)

class CompraForm(forms.ModelForm):
    class Meta:
        model = Compra
        fields = [
            'Com_Created',
            'Com_tipo',
            'Com_Cliente_ID',
            'Com_Precio',
            'Com_Cantidad',
            'Com_Cambista_ID',
        ]

        labels = {
            'Com_Created': 'Fecha de operacion',
            'Com_tipo': 'Tipo Compra',
            'Com_Cliente_ID': 'Cliente',
            'Com_Precio': 'Precio',
            'Com_Cantidad': 'Cantidad',
            'Com_Cambista_ID': 'Cambista',
        }

    widgets  =  {

                'Com_Created': forms.TextInput(attrs={'class':'form-control'}),
                'Com_tipo': forms.TextInput(attrs={'class':'form-control'}),
                'Com_Cliente_ID': forms.TextInput(attrs={'class':'form-control'}),
                'Com_Precio': forms.Select(attrs={'class':'form-control'}),
                'Com_Cantidad': forms.NumberInput(attrs={'class':'form-control'}),
                'Com_Cambista_ID': forms.TextInput(attrs={'class':'form-control'}),

        }
