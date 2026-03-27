# reportes/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('reportes/curso/<int:curso_id>/', views.ReporteCursoView.as_view(), name='reporte_curso'),
    path('reportes/estudiante/<int:estudiante_id>/', views.ReporteEstudianteView.as_view(), name='reporte_estudiante'),
]
