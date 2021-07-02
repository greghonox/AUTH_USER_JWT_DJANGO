from django.shortcuts import render
from rest_framework import viewsets
from .models import Todo, Pasciente, Portabilidade_Whatsapp
from .serializers import (
    TodoSerializer,
    PacientesSerializer,
    PortablidadeWhatsappSerializer,
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
