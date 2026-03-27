# calificaciones/views.py
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Calificacion
from .serializers import CalificacionSerializer
from usuarios.permissions import EsAdminOProfesor


class CalificacionViewSet(viewsets.ModelViewSet):
    """RF-014, RF-015, RF-017: CRUD de calificaciones."""
    queryset = Calificacion.objects.select_related('estudiante', 'curso').all()
    serializer_class = CalificacionSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
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

    @action(detail=False, methods=['get'], url_path='curso/(?P<curso_id>[^/.]+)')
    def por_curso(self, request, curso_id=None):
        """GET /api/calificaciones/curso/{id}/ — Notas de un curso."""
        calificaciones = self.get_queryset().filter(curso_id=curso_id)
        serializer = self.get_serializer(calificaciones, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'], url_path='estudiante/(?P<estudiante_id>[^/.]+)')
    def por_estudiante(self, request, estudiante_id=None):
        """GET /api/calificaciones/estudiante/{id}/ — Notas de un estudiante."""
        calificaciones = self.get_queryset().filter(estudiante_id=estudiante_id)
        serializer = self.get_serializer(calificaciones, many=True)
        return Response(serializer.data)
