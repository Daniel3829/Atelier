# matriculas/models.py
from django.db import models
from usuarios.models import Usuario
from cursos.models import Curso


class Matricula(models.Model):
    """RF-011: Matriculacion de estudiantes en cursos."""
    estudiante = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        related_name='matriculas',
        limit_choices_to={'rol': 'ESTUDIANTE'}
    )
    curso = models.ForeignKey(
        Curso,
        on_delete=models.CASCADE,
        related_name='matriculas'
    )
    fecha_matricula = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.estudiante.get_full_name()} - {self.curso.nombre}"

    class Meta:
        verbose_name = 'Matricula'
        verbose_name_plural = 'Matriculas'
        unique_together = ['estudiante', 'curso']
        ordering = ['-fecha_matricula']