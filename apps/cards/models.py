from django.db import models
from apps.users.models import User
#CardModel
class Card(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name="user_posts"
    )
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
    genres = models.CharField(
        max_length=255,
        verbose_name="Жанр"
    )
    descriptions = models.TextField(
        verbose_name="Описание"
    )
    
    def __str__(self):
        return f"Название: {self.title}, Тип: {self.type}, Год: {self.years}, Жанр: {self.genres}"
    
    class Meta:
        verbose_name  = "Манга"
        verbose_name_plural = "Манги"
        
#CommentModel

class CardComment(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name="user_comment"
    )
    card = models.ForeignKey(
        Card, on_delete=models.CASCADE,
        related_name="card_comments",
        verbose_name="Пост"
    )
    comment = models.CharField(
        max_length=255,
        verbose_name="Текст комментарий"
    )
    created = models.DateTimeField(
        auto_now_add=True,
        editable=True,
        
    )

    def __str__(self):
        return f"{self.user}, {self.comment}"

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"