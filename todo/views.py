from django.shortcuts import render
from rest_framework import filters, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.settings import api_settings
from rest_framework.views import APIView

from .models import Pasciente, Portabilidade_Whatsapp, Todo, UserProfile
from .permissions import UpdateOwnProfile
from .serializers import (
    PacientesSerializer,
    PortablidadeWhatsappSerializer,
    TodoSerializer,
    UserProfileSerializer,
)


class TodoView(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()


class PacientesView(viewsets.ModelViewSet):
    serializer_class = PacientesSerializer
    queryset = Pasciente.objects.all()


class Portabilidade_WhatsappView(viewsets.ModelViewSet):
    serializer_class = PortablidadeWhatsappSerializer
    queryset = Portabilidade_Whatsapp.objects.all()


class UserProfileVIewSet(viewsets.ModelViewSet):
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (UpdateOwnProfile, IsAuthenticated)
    filter_backends = (filters.SearchFilter,)
    search_fields = ("name", "email")
