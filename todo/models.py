from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models

# Create your models here.


class Todo(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    completed = models.BooleanField(default=False)

    def _str_(self):
        return self.title


class Pasciente(models.Model):
    sexo_choice = (("M", "Masculino"), ("F", "Feminino"))
    tp_parentesco = (
        ("H", "Nenhum"),
        ("T", "Tio(a)"),
        ("S", "Sobrinho(a)"),
        ("A", "Amigo(a)"),
        ("P", "Primo(a)"),
        ("I", "Irmão/Irmã"),
        ("J", "Cônjuge"),
        ("F", "Filho(a)"),
        ("C", "Cuidador(ra)"),
        ("O", "Outros"),
        ("N", "Neto(a)"),
    )
    nome = models.CharField(null=True, max_length=200, verbose_name="nome")
    sobrenome = models.CharField(max_length=200, verbose_name="sobrenome")
    data_nascimento = models.DateField(null=True, verbose_name="data nascimento")
    sexo = models.CharField(
        default=sexo_choice[0][0],
        max_length=1,
        choices=sexo_choice,
        verbose_name="Sexo",
    )
    medico = models.CharField(max_length=200, verbose_name="médico responsável")
    prontuario = models.IntegerField(verbose_name="número do prontuário", unique=True)
    convenio = models.CharField(max_length=200, verbose_name="convênio")
    whatsapp = models.CharField(
        null=True, max_length=15, verbose_name="número do whatsapp", unique=True
    )
    whatsapp_h = models.CharField(
        null=True,
        max_length=30,
        verbose_name="número do whatsapp higienizado",
        unique=True,
    )
    data_registro = models.DateField(
        auto_now_add=True, verbose_name="Data de Registro Paciente"
    )
    parentesco = models.CharField(
        default=tp_parentesco[0][0],
        max_length=1,
        choices=tp_parentesco,
        verbose_name="Grau parentesco",
    )
    nome_parente = models.CharField(
        max_length=200,
        verbose_name="Nome do parente",
        null=True,
        default="",
        blank=True,
    )

    class Meta:
        unique_together = (("prontuario", "whatsapp"),)

    def __str__(self):
        return f"{self.nome} {self.sobrenome} ({self.id})"


class Portabilidade_Whatsapp(models.Model):
    id_pasciente_origem = models.ForeignKey(
        Pasciente, on_delete=models.CASCADE, related_name="id_origem"
    )
    id_pasciente_destino = models.ForeignKey(
        Pasciente, on_delete=models.CASCADE, related_name="id_destino"
    )

    whatsapp = models.CharField(null=True, max_length=15)
    data_modificacao = models.DateField(auto_now_add=True)

    def __str__(self):
        return (
            f"{self.id_pasciente_origem} -> "
            f" {self.id_pasciente_destino} "
            f" {self.whatsapp} {self.data_modificacao}"
        )


class UserProfileManager(BaseUserManager):
    def create_user(self, name, email, password):
        if all(x == "" for x in [name, email, password]):
            raise ValueError(
                "ESTA FALTANDO O CAMPO {'\n'.join([str(x) for x in [usuario, email, password] if x == ''])}"
            )
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, name, email, password):
        user = self.create_user(name, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, verbose_name="email usuario", unique=True)
    name = models.CharField(max_length=200, verbose_name="nome usuario", null=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    objects = UserProfileManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name", "password"]

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name

    def __str__(self):
        return f"{self.id} {self.name} {self.email}"
