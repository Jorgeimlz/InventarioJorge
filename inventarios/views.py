from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .models import Producto, Categoria
from .forms import ProductoForm, CategoriaForm

class ProductoListView(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
    model = Producto
    template_name = 'inventarios/lista_productos.html'
    context_object_name = 'productos'
    permission_required = 'inventarios.can_view_product'

    def get_queryset(self):
        queryset = super().get_queryset()
        categoria_id = self.request.GET.get('categoria')
        if categoria_id:
            queryset = queryset.filter(categoria_id=categoria_id)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias'] = Categoria.objects.all()
        return context

class ProductoCreateView(LoginRequiredMixin, PermissionRequiredMixin, generic.CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'inventarios/producto_form.html'
    success_url = reverse_lazy('inventarios:productos_list')
    permission_required = 'inventarios.can_create_product'

class ProductoUpdateView(LoginRequiredMixin, PermissionRequiredMixin, generic.UpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'inventarios/producto_form.html'
    success_url = reverse_lazy('inventarios:productos_list')
    permission_required = 'inventarios.change_producto'

class ProductoDeleteView(LoginRequiredMixin, PermissionRequiredMixin, generic.DeleteView):
    model = Producto
    template_name = 'inventarios/producto_confirm_delete.html'
    success_url = reverse_lazy('inventarios:productos_list')
    permission_required = 'inventarios.delete_producto'

class CategoriaListView(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
    model = Categoria
    template_name = 'inventarios/lista_categorias.html'
    context_object_name = 'categorias'
    permission_required = 'inventarios.view_categoria'

class CategoriaCreateView(LoginRequiredMixin, PermissionRequiredMixin, generic.CreateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'inventarios/categoria_form.html'
    success_url = reverse_lazy('inventarios:categorias_list')
    permission_required = 'inventarios.add_categoria'

class CategoriaUpdateView(LoginRequiredMixin, PermissionRequiredMixin, generic.UpdateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'inventarios/categoria_form.html'
    success_url = reverse_lazy('inventarios:categorias_list')
    permission_required = 'inventarios.change_categoria'

class CategoriaDeleteView(LoginRequiredMixin, PermissionRequiredMixin, generic.DeleteView):
    model = Categoria
    template_name = 'inventarios/categoria_confirm_delete.html'
    success_url = reverse_lazy('inventarios:categorias_list')
    permission_required = 'inventarios.delete_categoria'

def custom_permission_denied_view(request, exception=None):
    return render(request, '403.html', status=403)


