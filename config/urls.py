# config/urls.py
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    # Django Admin
    path('admin/', admin.site.urls),

    # === API Endpoints ===
    # Auth: /api/auth/register/, /api/auth/login/, /api/auth/logout/, /api/auth/recuperar-password/
    # Usuarios: /api/usuarios/
    path('api/', include('usuarios.urls')),

    # Cursos: /api/cursos/, Periodos: /api/periodos/
    path('api/', include('cursos.urls')),

    # Matriculas: /api/matriculas/
    path('api/', include('matriculas.urls')),

    # Calificaciones: /api/calificaciones/, /api/calificaciones/curso/{id}/, /api/calificaciones/estudiante/{id}/
    path('api/', include('calificaciones.urls')),

    # Reportes: /api/reportes/curso/{id}/, /api/reportes/estudiante/{id}/
    path('api/', include('reportes.urls')),

    # === Frontend Templates ===
    path('', TemplateView.as_view(template_name='auth/code.html'), name='login_page'),
    path('dashboard/admin/', TemplateView.as_view(template_name='admin/admin.html'), name='admin_dashboard'),
    path('dashboard/admin/usuarios/', TemplateView.as_view(template_name='admin/admin_usuarios.html'), name='admin_usuarios'),
    path('dashboard/admin/cursos/', TemplateView.as_view(template_name='admin/admin_cursos.html'), name='admin_cursos'),
    path('dashboard/profesor/cursos/', TemplateView.as_view(template_name='profesor/prof_cursos.html'), name='prof_cursos'),
    path('dashboard/profesor/notas/', TemplateView.as_view(template_name='profesor/prof_notas.html'), name='prof_notas'),
    path('dashboard/estudiante/cursos/', TemplateView.as_view(template_name='estudiante/estudiantes_cursos.html'), name='estudiante_cursos'),
]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)