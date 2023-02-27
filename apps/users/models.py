from django.db import models

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    profile_image = models.ImageField(
        upload_to="profile_images/",
        verbose_name="Фотография профиля",
        blank=True,null=True
    )
    bio = models.CharField(
        max_length=255,
        verbose_name="Описание",
        blank=True,null=True,
        help_text="Напишите описаие профиля, по умолчанию можно не заполнять"
    )
    
    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"