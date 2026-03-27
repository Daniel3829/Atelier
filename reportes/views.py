# reportes/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from usuarios.models import Usuario
from cursos.models import Curso
from matriculas.models import Matricula
from calificaciones.models import Calificacion
from usuarios.serializers import UsuarioSerializer
from calificaciones.serializers import CalificacionSerializer


class ReporteCursoView(APIView):
    """RF-019: Listado de estudiantes por curso con calificaciones."""
    permission_classes = [IsAuthenticated]

    def get(self, request, curso_id):
        try:
            curso = Curso.objects.get(id=curso_id)
        except Curso.DoesNotExist:
            return Response({'error': 'Curso no encontrado.'}, status=404)

        # Obtener estudiantes matriculados
        matriculas = Matricula.objects.filter(curso=curso).select_related('estudiante')
        estudiantes = [m.estudiante for m in matriculas]

        # Obtener calificaciones
        calificaciones = Calificacion.objects.filter(curso=curso).select_related('estudiante')

        # Calcular promedio del curso
        notas = [c.nota_final for c in calificaciones]
        promedio_curso = round(sum(notas) / len(notas), 2) if notas else 0

        return Response({
            'curso': {
                'id': curso.id,
                'codigo': curso.codigo,
                'nombre': curso.nombre,
                'profesor': curso.profesor.get_full_name() if curso.profesor else None,
            },
            'total_estudiantes': len(estudiantes),
            'promedio_curso': promedio_curso,
            'estudiantes': UsuarioSerializer(estudiantes, many=True).data,
            'calificaciones': CalificacionSerializer(calificaciones, many=True).data,
        })


class ReporteEstudianteView(APIView):
    """RF-020, RF-021: Reporte de calificaciones y resumen academico de un estudiante."""
    permission_classes = [IsAuthenticated]

    def get(self, request, estudiante_id):
        try:
            estudiante = Usuario.objects.get(id=estudiante_id)
        except Usuario.DoesNotExist:
            return Response({'error': 'Estudiante no encontrado.'}, status=404)

        calificaciones = Calificacion.objects.filter(
            estudiante=estudiante
        ).select_related('curso')

        # Calcular promedio general
        notas = [c.nota_final for c in calificaciones]
        promedio_general = round(sum(notas) / len(notas), 2) if notas else 0

        # Cursos matriculados
        matriculas = Matricula.objects.filter(
            estudiante=estudiante
        ).select_related('curso')

        return Response({
            'estudiante': UsuarioSerializer(estudiante).data,
            'total_cursos': matriculas.count(),
            'promedio_general': promedio_general,
            'calificaciones': CalificacionSerializer(calificaciones, many=True).data,
            'cursos': [
                {
                    'id': m.curso.id,
                    'codigo': m.curso.codigo,
                    'nombre': m.curso.nombre,
                    'fecha_matricula': m.fecha_matricula,
                }
                for m in matriculas
            ],
        })
