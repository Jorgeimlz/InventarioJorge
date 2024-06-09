from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from inventarios.views import custom_permission_denied_view

handler403 = custom_permission_denied_view

urlpatterns = [
    path('admin/logout/', auth_views.LogoutView.as_view(next_page='/admin/login/?next=/admin/'), name='admin_logout'),
    path('admin/', admin.site.urls),
    path('inventarios/', include(('inventarios.urls', 'inventarios'), namespace='inventarios')),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
]


