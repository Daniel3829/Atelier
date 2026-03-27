# usuarios/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'usuarios', views.UsuarioViewSet)

urlpatterns = [
    # Autenticacion
    path('auth/register/', views.RegistroView.as_view(), name='registro'),
    path('auth/login/', views.LoginView.as_view(), name='login'),
    path('auth/logout/', views.LogoutView.as_view(), name='logout'),
    path('auth/recuperar-password/', views.RecuperarPasswordView.as_view(), name='recuperar_password'),
    # CRUD Usuarios
    path('', include(router.urls)),
]
