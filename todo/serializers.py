from rest_framework import serializers

from .models import Pasciente, Portabilidade_Whatsapp, Todo, UserProfile


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


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ("id", "name", "email", "password")
        extra_kwargs = {
            "password": {"write_only": True, "style": {"input_type": "password"}}
        }

    def create(self, request):
        user = UserProfile.objects.create_user(
            name=request["name"],
            email=request["email"],
            password=request["password"],
        )
        return user

    def update(self, instance, request):
        password = request["password"]
        instance.set_password(password)
        return super().update(instance, request)
