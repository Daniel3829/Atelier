# usuarios/views.py
from rest_framework import viewsets, status, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Usuario
from .serializers import UsuarioSerializer, RegistroSerializer, LoginSerializer
from .permissions import EsAdmin


class RegistroView(generics.CreateAPIView):
    """RF-001: Registro de usuarios."""
    queryset = Usuario.objects.all()
    serializer_class = RegistroSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # RF-enrollment: Set is_active based on creator's role
        is_admin = request.user.is_authenticated and getattr(request.user, 'rol', None) == 'ADMIN'
        user = serializer.save(is_active=is_admin)
        # Generar tokens JWT para el nuevo usuario
        refresh = RefreshToken.for_user(user)
        return Response({
            'mensaje': 'Usuario registrado exitosamente.' if is_admin else 'Solicitud de registro enviada. Un administrador la revisará.',
            'user': UsuarioSerializer(user).data,
            'tokens': {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }
        }, status=status.HTTP_201_CREATED)


class LoginView(APIView):
    """RF-002: Inicio de sesion."""
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data, status=status.HTTP_200_OK)


class LogoutView(APIView):
    """RF-004: Cierre de sesion seguro (blacklist del refresh token)."""
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data.get('refresh')
            if refresh_token:
                token = RefreshToken(refresh_token)
                token.blacklist()
            return Response(
                {'mensaje': 'Sesion cerrada exitosamente.'},
                status=status.HTTP_200_OK
            )
        except Exception:
            return Response(
                {'error': 'Token invalido.'},
                status=status.HTTP_400_BAD_REQUEST
            )


class RecuperarPasswordView(APIView):
    """RF-005: Recuperacion de contrasena (placeholder)."""
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get('email')
        if not email:
            return Response(
                {'error': 'El email es requerido.'},
                status=status.HTTP_400_BAD_REQUEST
            )
        # Verificar que el usuario existe
        if not Usuario.objects.filter(email=email).exists():
            return Response(
                {'error': 'No existe un usuario con ese email.'},
                status=status.HTTP_404_NOT_FOUND
            )
        return Response(
            {'mensaje': 'Se ha enviado un enlace de recuperacion al correo.'},
            status=status.HTTP_200_OK
        )


class UsuarioViewSet(viewsets.ModelViewSet):
    """RF-006, RF-007, RF-008: CRUD de usuarios (solo admin)."""
    queryset = Usuario.objects.all().order_by('-date_joined')
    serializer_class = UsuarioSerializer
    permission_classes = [IsAuthenticated, EsAdmin]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance == request.user:
            return Response(
                {'error': 'No puedes eliminar tu propia cuenta.'},
                status=status.HTTP_400_BAD_REQUEST
            )
        self.perform_destroy(instance)
        return Response(
            {'mensaje': 'Usuario eliminado exitosamente.'},
            status=status.HTTP_204_NO_CONTENT
        )
