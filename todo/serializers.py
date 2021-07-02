from rest_framework import serializers
from .models import Todo, Pasciente, Portabilidade_Whatsapp


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ("id", "title", "description", "completed")


class PacientesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pasciente
        fields = "__all__"


class PortablidadeWhatsappSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portabilidade_Whatsapp
        fields = "__all__"
