from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, DeleteView, UpdateView, DetailView
#from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.http import HttpResponse
from changehouse.models import Cliente, Compra
from changehouse.forms import ClienteForm, CompraForm

def inicio(request):
    return render(request, "base/base.html", {})


# Vistar para crear un cliente
class ClienteCreateView(CreateView):
    model = Cliente
    template_name = 'clientes/add_cliente.html'
    form_class = ClienteForm
    redirect_field_name = 'redirect_to'
    success_url = reverse_lazy('site:cliente_listar')

# Vista para listar los clientes
class ClienteListView(ListView):
    template_name = 'clientes/list_cliente.html'
    redirect_field_name = 'redirect_to'
    # Se descomenta la linea de abajo para que funcione el paginado, sin Datables.
    #paginate_by = 5
    def get_queryset(self):
        return Cliente.objects.filter(Cli_Estado=0)

#Vista para editar un Cliente
class ClienteUpdateView(UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'clientes/update_cliente.html'
    success_url = reverse_lazy('site:cliente_listar')

# Vista para eliminar un cliente
class ClienteDeleteView(DeleteView):
    #queryset = Estudiante.objects.update(Es_Estado=1)
    model = Cliente
    template_name = 'clientes/delete_cliente.html'
    success_url = reverse_lazy('site:cliente_listar')
    redirect_field_name = 'redirect_to'


# Vista para hacer una vista detalle
class ClienteDetailView(DetailView):
    model = Cliente
    template_name = 'clientes/show_cliente.html'
    redirect_field_name = 'redirect_to'



# Vista para registrar una Compra
class CompraCreateView(CreateView):
    model = Compra
    template_name = 'compras/add_compra.html'
    form_class = CompraForm
    redirect_field_name = 'redirect_to'
    success_url = reverse_lazy('site:cliente_listar')
