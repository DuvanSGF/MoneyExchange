from django.urls import path, include

from . import views
#from changehouse.views import *

app_name = 'changehouse'
urlpatterns = [
    path('', views.inicio, name='inicio'),
]
