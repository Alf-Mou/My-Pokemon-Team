from django.db import models

class Pokemon(models.Model):
    nome = models.CharField(max_length=50)
    altura = models.FloatField()
    peso = models.FloatField()
    titulo = models.CharField(max_length=50)
    descricao = models.TextField(max_length=400)
    tipo_primario = models.CharField(max_length=15)
    tipo_secundario = models.CharField(max_length=15, blank=True, null=True)
    hp = models.IntegerField()
    ataque = models.IntegerField()
    defesa = models.IntegerField()
    sp_ataque = models.IntegerField()
    sp_defesa = models.IntegerField()
    velocidade = models.IntegerField()
    stats_total = models.IntegerField()
    imagem = models.CharField(max_length=50)
    estagio_um = models.CharField(max_length=50)
    estagio_dois = models.CharField(max_length=50)
    estagio_tres = models.CharField(max_length=50)

    def __str__(self):
        return f"Pokemon [pokemon={self.nome}]"
    
    