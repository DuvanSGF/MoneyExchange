from django.urls import path, include, re_path
from changehouse.views import *
from django.contrib.auth import views as auth_views
from .views import (
    HomePageView,
    ClienteCreateView,
    ClienteListView,
    ClienteUpdateView,
    ClienteDeleteView,
    ClienteDetailView,
    CompraCreateView,
    reportView,
    LoginPageView)
from .import views

urlpatterns = [
    path('', HomePageView.as_view(), name='inicio'),
    path('login/', LoginPageView.as_view(), name='login'),
    path('nuevo/', ClienteCreateView.as_view(), name='cliente_crear'),
    path('listar/', ClienteListView.as_view(), name='cliente_listar'),
    path('mostrar/<int:pk>/', ClienteDetailView.as_view(), name='cliente_mostrar'),
    path('editar/<int:pk>/', ClienteUpdateView.as_view(), name='cliente_editar'),
    path('eliminar/<int:pk>/', ClienteDeleteView.as_view(), name='cliente_eliminar'),
    #url('editar/(?P<pk>\d+)/$', EstudianteUpdate.as_view(), name='estudiante_editar'),
    #re_path(r'editar/(?P<pk>\d+)/$',  ClienteDeleteView.as_view(), name='cliente_eliminar'),
    path('compra/', CompraCreateView.as_view(), name='compra_crear'),
     path('compralistar/', CompraListView.as_view(), name='compra_listar'),

     path('venta/', VentaCreateView.as_view(), name='venta_crear'),
     path('ventalistar/', VentaListView.as_view(), name='venta_listar'),

 path('reporte/', reportView.as_view(), name='reporte'),
]
