from django.db import models

class Usuarios (models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=200)
    email = models.TextField(max_length=200)