from django.db import models

class Pokemon(models.Model):

    OPCOES_TIPOS = [
        ("NORMAL","Normal"),
        ("FIRE","Fire"),
        ("WATER","Water"),
        ("ELECTRIC","Electric"),
        ("GRASS","Grass"),
        ("ICE","Ice"),
        ("FIGHTING","Fighting"),
        ("POISON","Poison"),
        ("GROUND","Ground"),
        ("FLYING","Flying"),
        ("PSYCHIC","Psychic"),
        ("BUG","Bug"),
        ("ROCK","Rock"),
        ("GHOST","Ghost"),
        ("DRAGON","Dragon"),
        ("DARK","Dark"),
        ("STEEL","Steel"),
        ("FAIRY","Fairy"),
    ]


    nome = models.CharField(max_length=50)
    altura = models.FloatField()
    peso = models.FloatField()
    titulo = models.CharField(max_length=50)
    descricao = models.TextField(max_length=800)
    tipo_primario = models.CharField(max_length=20, choices=OPCOES_TIPOS, default="")
    tipo_secundario = models.CharField(max_length=20, choices=OPCOES_TIPOS, default="", blank=True, null=True)
    hp = models.IntegerField()
    ataque = models.IntegerField()
    defesa = models.IntegerField()
    sp_ataque = models.IntegerField()
    sp_defesa = models.IntegerField()
    velocidade = models.IntegerField()
    stats_total = models.IntegerField()
    imagem = models.CharField(max_length=50)
    estagio_um_img = models.CharField(max_length=50)
    estagio_um_nome = models.CharField(max_length=50)
    estagio_dois_img = models.CharField(max_length=50)
    estagio_dois_nome = models.CharField(max_length=50)
    estagio_tres_img = models.CharField(max_length=50)
    estagio_tres_nome = models.CharField(max_length=50)
    imagem_index = models.CharField(max_length=50)
    def __str__(self):
        return f"Pokemon [pokemon={self.nome}]"
    
    