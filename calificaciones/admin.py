# calificaciones/admin.py
from django.contrib import admin
from .models import Calificacion


@admin.register(Calificacion)
class CalificacionAdmin(admin.ModelAdmin):
    list_display = ['estudiante', 'curso', 'notas', 'nota_final']
    list_filter = ['curso']
    search_fields = ['estudiante__username', 'estudiante__first_name', 'curso__nombre']
