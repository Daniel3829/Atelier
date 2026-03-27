# matriculas/admin.py
from django.contrib import admin
from .models import Matricula


@admin.register(Matricula)
class MatriculaAdmin(admin.ModelAdmin):
    list_display = ['estudiante', 'curso', 'fecha_matricula']
    list_filter = ['curso']
    search_fields = ['estudiante__username', 'estudiante__first_name', 'curso__nombre']
