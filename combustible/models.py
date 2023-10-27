from django.db import models


class Mark(models.Model):
    description = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = "Marca"
        verbose_name_plural = "Marcas"
