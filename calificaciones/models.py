# calificaciones/models.py
from django.db import models
from usuarios.models import Usuario
from cursos.models import Curso


class Calificacion(models.Model):
    """RF-014, RF-016: Calificaciones con multiples notas."""
    estudiante = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        related_name='calificaciones',
        limit_choices_to={'rol': 'ESTUDIANTE'}
    )
    curso = models.ForeignKey(
        Curso,
        on_delete=models.CASCADE,
        related_name='calificaciones'
    )
    notas = models.JSONField(default=list, verbose_name='Notas')

    @property
    def nota_final(self):
        """RF-018: Calculo automatico del promedio final."""
        if not self.notas:
            return 0.0
        try:
            total = sum(float(n) for n in self.notas)
            return round(total / len(self.notas), 2)
        except (ValueError, TypeError):
            return 0.0

    def __str__(self):
        return f"{self.estudiante.get_full_name()} - {self.curso.nombre}: {self.nota_final}"

    class Meta:
        verbose_name = 'Calificacion'
        verbose_name_plural = 'Calificaciones'
        unique_together = ['estudiante', 'curso']