from django.db import models

class Paciente(models.Model):
    nome = models.CharField(max_length=150, verbose_name="Nome Completo")
    idade = models.PositiveIntegerField(verbose_name="Idade")
    telefone = models.CharField(max_length=20, verbose_name="Telefone")
    criado_em = models.DateTimeField(auto_now_add=True, verbose_name="Data de Cadastro")

    class Meta:
        verbose_name = "Paciente"
        verbose_name_plural = "Pacientes"
        ordering = ['-criado_em']

    def __str__(self):
        return f"{self.nome} - {self.idade} anos"