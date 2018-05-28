from django.db import models

# Create your models here.

class Agenda(models.Model):
	agenda_id = models.AutoField(primary_key=True)
	nome = models.CharField(max_length=255)
	telefone = models.CharField(max_length=255)
	publicado = models.BooleanField(default=False)

	def __str__(self):
		return self.nome