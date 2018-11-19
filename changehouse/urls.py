from django.urls import path, include
from changehouse.views import *
from . import views
from django.contrib.auth import views as auth_views
#from changehouse.views import *

app_name = 'changehouse'
urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nuevo/', ClienteCreate.as_view(), name='cliente_crear'),
    path('listar/', ClienteList.as_view(), name='cliente_listar'),
]
