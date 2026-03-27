# calificaciones/serializers.py
from rest_framework import serializers
from .models import Calificacion


class CalificacionSerializer(serializers.ModelSerializer):
    nota_final = serializers.FloatField(read_only=True)
    estudiante_nombre = serializers.SerializerMethodField()
    curso_nombre = serializers.SerializerMethodField()
    curso_duracion = serializers.SerializerMethodField()

    class Meta:
        model = Calificacion
        fields = [
            'id', 'estudiante', 'estudiante_nombre',
            'curso', 'curso_nombre', 'curso_duracion',
            'notas', 'nota_final'
        ]
        read_only_fields = ['id']

    def validate_notas(self, value):
        if not isinstance(value, list):
            raise serializers.ValidationError("Las notas deben estar en formato de lista.")
        for nota in value:
            try:
                n = float(nota)
                if n < 0.0 or n > 5.0:
                    raise serializers.ValidationError("Cada nota debe estar entre 0.0 y 5.0.")
            except (ValueError, TypeError):
                raise serializers.ValidationError("Todas las notas deben ser valores numéricos.")
        # Ensure they are stored as floats
        return [float(n) for n in value]

    def get_estudiante_nombre(self, obj):
        return obj.estudiante.get_full_name() or obj.estudiante.username

    def get_curso_nombre(self, obj):
        return obj.curso.nombre

    def get_curso_duracion(self, obj):
        return obj.curso.duracion
