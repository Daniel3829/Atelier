# matriculas/serializers.py
from rest_framework import serializers
from .models import Matricula


class MatriculaSerializer(serializers.ModelSerializer):
    estudiante_nombre = serializers.SerializerMethodField()
    curso_nombre = serializers.SerializerMethodField()

    class Meta:
        model = Matricula
        fields = [
            'id', 'estudiante', 'estudiante_nombre',
            'curso', 'curso_nombre', 'fecha_matricula'
        ]
        read_only_fields = ['id', 'fecha_matricula']

    def get_estudiante_nombre(self, obj):
        return obj.estudiante.get_full_name() or obj.estudiante.username

    def get_curso_nombre(self, obj):
        return obj.curso.nombre
