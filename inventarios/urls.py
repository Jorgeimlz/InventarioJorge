from django.urls import path
from .views import (
    ProductoListView,
    ProductoCreateView,
    ProductoUpdateView,
    ProductoDeleteView,
    CategoriaListView,
    CategoriaCreateView,
    CategoriaUpdateView,
    CategoriaDeleteView,
)

app_name = 'inventarios'

urlpatterns = [
    path('productos/', ProductoListView.as_view(), name='productos_list'),
    path('productos/nuevo/', ProductoCreateView.as_view(), name='productos_create'),
    path('productos/<int:pk>/editar/', ProductoUpdateView.as_view(), name='productos_update'),
    path('productos/<int:pk>/eliminar/', ProductoDeleteView.as_view(), name='productos_delete'),
    path('categorias/', CategoriaListView.as_view(), name='categorias_list'),
    path('categorias/nuevo/', CategoriaCreateView.as_view(), name='categorias_create'),
    path('categorias/<int:pk>/editar/', CategoriaUpdateView.as_view(), name='categorias_update'),
    path('categorias/<int:pk>/eliminar/', CategoriaDeleteView.as_view(), name='categorias_delete'),
]



