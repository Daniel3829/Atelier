# cursos/views.py
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Curso
from .serializers import CursoSerializer
from usuarios.permissions import EsAdmin, EsAdminOProfesor


class CursoViewSet(viewsets.ModelViewSet):
    """RF-009, RF-010, RF-012: CRUD de cursos."""
    queryset = Curso.objects.select_related('profesor').all()
    serializer_class = CursoSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAuthenticated(), EsAdmin()]
        return [IsAuthenticated()]

    def get_queryset(self):
        qs = super().get_queryset()
        user = self.request.user

        # Profesores ven solo sus cursos asignados
        if user.rol == 'PROFESOR':
            return qs.filter(profesor=user)
        # Estudiantes ven solo cursos donde estan matriculados
        if user.rol == 'ESTUDIANTE':
            return qs.filter(matricula__estudiante=user).distinct()
        # Admin ve todo
        return qs