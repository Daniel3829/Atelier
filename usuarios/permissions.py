# usuarios/permissions.py
from rest_framework.permissions import BasePermission


class EsAdmin(BasePermission):
    """Permite acceso solo a usuarios con rol ADMIN."""
    def has_permission(self, request, view):
        return (
            request.user
            and request.user.is_authenticated
            and (request.user.rol == 'ADMIN' or request.user.is_superuser)
        )


class EsProfesor(BasePermission):
    """Permite acceso solo a usuarios con rol PROFESOR."""
    def has_permission(self, request, view):
        return (
            request.user
            and request.user.is_authenticated
            and request.user.rol == 'PROFESOR'
        )


class EsEstudiante(BasePermission):
    """Permite acceso solo a usuarios con rol ESTUDIANTE."""
    def has_permission(self, request, view):
        return (
            request.user
            and request.user.is_authenticated
            and request.user.rol == 'ESTUDIANTE'
        )


class EsAdminOProfesor(BasePermission):
    """Permite acceso a ADMIN o PROFESOR."""
    def has_permission(self, request, view):
        return (
            request.user
            and request.user.is_authenticated
            and (request.user.rol in ['ADMIN', 'PROFESOR'] or request.user.is_superuser)
        )
