# usuarios/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models


class Usuario(AbstractUser):
    ROLES = (
        ('ADMIN', 'Administrador'),
        ('PROFESOR', 'Profesor'),
        ('ESTUDIANTE', 'Estudiante'),
    )

    identificacion = models.CharField(max_length=20, unique=True)
    telefono = models.CharField(max_length=15, blank=True, default='')
    rol = models.CharField(max_length=15, choices=ROLES, default='ESTUDIANTE')

    def __str__(self):
        return f"{self.get_full_name()} ({self.rol})"

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'