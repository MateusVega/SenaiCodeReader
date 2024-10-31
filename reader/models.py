from django.db import models

class ferramentas(models.Model):
    numero = models.TextField(max_length=255)
    nome = models.TextField(max_length=255)
    local = models.TextField(max_length=255)
    instrutor = models.TextField(max_length=255)
    status = models.TextField(max_length=255)

    def save(self, *args, **kwargs):
        super(ferramentas, self).save(*args, **kwargs)