from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.http import HttpResponse
from changehouse.models import Cliente
from changehouse.forms import ClienteForm

def inicio(request):
    return render(request, "base/base.html", {})


# Vistar para crear un cliente
class ClienteCreate(CreateView):
    model = Cliente
    template_name = 'clientes/add_cliente.html'
    form_class = ClienteForm
    redirect_field_name = 'redirect_to'
    success_url = reverse_lazy('site:inicio')

# Vista para Listar los estudiantes
class ClienteList(ListView):
    #queryset = Estudiante.objects.order_by('id_Estudiante')
    template_name = 'clientes/list_cliente.html'
    redirect_field_name = 'redirect_to'
    # Se descomenta la linea de abajo para que funcione el paginado, sin Datables.
    #paginate_by = 5
    def get_queryset(self):
        return Cliente.objects.filter(Cli_Estado=0)
