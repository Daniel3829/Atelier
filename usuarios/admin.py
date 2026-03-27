# usuarios/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario


@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
    list_display = ['username', 'email', 'first_name', 'last_name', 'rol', 'identificacion', 'is_active']
    list_filter = ['rol', 'is_active']
    search_fields = ['username', 'email', 'first_name', 'last_name', 'identificacion']
    fieldsets = UserAdmin.fieldsets + (
        ('Informacion adicional', {
            'fields': ('identificacion', 'telefono', 'rol'),
        }),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Informacion adicional', {
            'fields': ('identificacion', 'telefono', 'rol'),
        }),
    )
