from django.db import models

# Create your models here.
class Manga(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Название"
    )
    type = models.CharField(
        max_length=255,
        verbose_name="Тип"
    )
    years = models.CharField(
        max_length=255,
        verbose_name="Год"
    )
    genre = models.CharField(
        max_length=255,
        verbose_name="Жанр"
    )
    descriptions = models.TextField(
        verbose_name="Описание"
    )
    
    def __str__(self):
        return f"Название: {self.title}, Тип: {self.type}, Год: {self.years}, Жанр: {self.genre}"
    
    class Meta:
        verbose_name  = "Манга"
        verbose_name_plural = "Манги"