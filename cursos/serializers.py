# cursos/serializers.py
from rest_framework import serializers
from .models import Curso
from usuarios.serializers import UsuarioSerializer


class CursoSerializer(serializers.ModelSerializer):
    profesor_nombre = serializers.SerializerMethodField()

    class Meta:
        model = Curso
        fields = [
            'id', 'codigo', 'nombre', 'descripcion', 'imagen',
            'profesor', 'profesor_nombre',
            'duracion'
        ]

    def get_profesor_nombre(self, obj):
        if obj.profesor:
            return obj.profesor.get_full_name() or obj.profesor.username
        return None