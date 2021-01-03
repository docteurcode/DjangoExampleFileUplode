from django.db import models


class FileUplode(models.Model):
	file = models.FileField()

	def __str__(self):
		return str(self.id)+ '# - '+ str(self.file.name)