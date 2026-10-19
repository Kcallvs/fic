from django.db import models
from apps.usuarios.models import Usuario

class Area(models.Model):
    nome = models.CharField("Nome", max_length=50)
    def __str__(self):
        return self.nome

class PublicoAlvo(models.Model):
    nome = models.CharField("Nome", max_length=50)
    def __str__(self):
        return self.nome    

class Curso(models.Model):
    titulo = models.CharField("Título", max_length=100)
    descricao = models.TextField("Descrição")
    ch = models.IntegerField("Carga-horária")
    data = models.DateField("Data de início", null=True, blank=True)
    vagas = models.IntegerField("Vagas")
    imagem = models.ImageField("Imagem", upload_to='cursos/', null=True, blank=True)
    area = models.ForeignKey(Area, on_delete=models.PROTECT)
    publicos = models.ManyToManyField(PublicoAlvo)
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT, null=True, blank=True)
    def __str__(self):
        return self.titulo
