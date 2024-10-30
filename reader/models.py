from django.db import models

class ferramentas(models.Model):
    nome = models.TextField(max_length=255)
    status = models.TextField(max_length=255)

    def save(self, *args, **kwargs):
        if ferramentas.objects.filter(nome=self.nome).exists():
            pass
        else:
            super(ferramentas, self).save(*args, **kwargs)