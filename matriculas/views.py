# matriculas/views.py
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Matricula
from .serializers import MatriculaSerializer
from usuarios.permissions import EsAdmin, EsAdminOProfesor


class MatriculaViewSet(viewsets.ModelViewSet):
    """RF-011: Gestion de matriculas."""
    queryset = Matricula.objects.select_related('estudiante', 'curso').all()
    serializer_class = MatriculaSerializer

    def get_permissions(self):
        if self.action in ['create', 'destroy']:
            return [IsAuthenticated(), EsAdminOProfesor()]
        return [IsAuthenticated()]

    def get_queryset(self):
        qs = super().get_queryset()
        user = self.request.user

        if user.rol == 'ESTUDIANTE':
            return qs.filter(estudiante=user)
        if user.rol == 'PROFESOR':
            return qs.filter(curso__profesor=user)
        return qs
