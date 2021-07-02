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
