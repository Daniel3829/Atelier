# usuarios/serializers.py
from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Usuario


class UsuarioSerializer(serializers.ModelSerializer):
    """Serializer completo para CRUD de usuarios."""
    class Meta:
        model = Usuario
        fields = [
            'id', 'username', 'email', 'first_name', 'last_name',
            'identificacion', 'telefono', 'rol', 'is_active', 'date_joined'
        ]
        read_only_fields = ['id', 'date_joined']


class RegistroSerializer(serializers.ModelSerializer):
    """Serializer para registro de nuevos usuarios."""
    password = serializers.CharField(write_only=True, min_length=6)

    class Meta:
        model = Usuario
        fields = [
            'username', 'email', 'password', 'first_name', 'last_name',
            'identificacion', 'telefono', 'rol'
        ]

    def create(self, validated_data):
        is_active = validated_data.pop('is_active', False)
        user = Usuario.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            identificacion=validated_data.get('identificacion', ''),
            telefono=validated_data.get('telefono', ''),
            rol=validated_data.get('rol', 'ESTUDIANTE'),
        )
        user.is_active = is_active
        user.save()
        return user


class LoginSerializer(serializers.Serializer):
    """Serializer para inicio de sesion con email/username y password."""
    email = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        email_or_username = data.get('email')
        password = data.get('password')

        # Intentar buscar por email primero, luego por username
        try:
            # Usar filter().first() para evitar MultipleObjectsReturned si hay duplicados por error
            user = Usuario.objects.filter(email=email_or_username).first()
            if user:
                username = user.username
            else:
                username = email_or_username
        except Exception:
            username = email_or_username

        user = authenticate(username=username, password=password)

        if user is None:
            raise serializers.ValidationError('Credenciales invalidas.')
        if not user.is_active:
            raise serializers.ValidationError('Cuenta desactivada.')

        refresh = RefreshToken.for_user(user)
        return {
            'user': UsuarioSerializer(user).data,
            'tokens': {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }
        }
