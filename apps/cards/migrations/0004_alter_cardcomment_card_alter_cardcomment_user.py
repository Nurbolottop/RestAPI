# Generated by Django 4.1.7 on 2023-02-26 06:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cards', '0003_alter_cardcomment_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cardcomment',
            name='card',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='card_comments', to='cards.card', verbose_name='Пост'),
        ),
        migrations.AlterField(
            model_name='cardcomment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_comment', to=settings.AUTH_USER_MODEL),
        ),
    ]
