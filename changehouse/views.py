from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, DeleteView, UpdateView, DetailView
#from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.http import HttpResponse
from changehouse.models import Cliente, Compra, Venta
from changehouse.forms import ClienteForm, CompraForm, VentaForm


from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import *;

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
    success_url = reverse_lazy('site:compra_listar')


# Vista para listar las compras
class CompraListView(ListView):
    template_name = 'compras/list_compra.html'
    redirect_field_name = 'redirect_to'
    # Se descomenta la linea de abajo para que funcione el paginado, sin Datables.
    #paginate_by = 5
    def get_queryset(self):
        return Compra.objects.all()


# Vista para registrar una ventas
class VentaCreateView(CreateView):
    model = Venta
    template_name = 'ventas/add_venta.html'
    form_class = VentaForm
    redirect_field_name = 'redirect_to'
    success_url = reverse_lazy('site:compra_listar')

# Vista para listar las ventas
class VentaListView(ListView):
    template_name = 'ventas/list_venta.html'
    redirect_field_name = 'redirect_to'
    # Se descomenta la linea de abajo para que funcione el paginado, sin Datables.
    #paginate_by = 5
    def get_queryset(self):
        return Venta.objects.all()


# Vista para Generar Reporte PDF
def report(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposicion'] = 'attachment; filename=Reporte'

    buffer = BytesIO()
    c = canvas.Canvas(buffer)

    # Header
    c.setLineWidth(.3)
    c.setFont('Helvetica', 22)
    c.drawString(30,750,'Ing. Duván Mejia Cortes')

    c.setFont('Helvetica', 12)
    c.drawString(30,735,'Report')

    c.setFont('Helvetica-Bold', 12)
    c.drawString(480,750, "25/08/2019")
    c.line(460,747,560,747)

    c.save()
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    return response
