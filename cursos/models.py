# cursos/models.py
from django.db import models
from usuarios.models import Usuario


class Curso(models.Model):
    """RF-009: Curso o materia."""
    codigo = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, default='')
    imagen = models.ImageField(upload_to='cursos/', null=True, blank=True)
    profesor = models.ForeignKey(
        Usuario,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='cursos_asignados',
        limit_choices_to={'rol': 'PROFESOR'}
    )
    duracion = models.PositiveSmallIntegerField(default=1, help_text="Duración en meses (1-12)")

    def __str__(self):
        return f"{self.codigo} - {self.nombre}"

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        ordering = ['codigo']