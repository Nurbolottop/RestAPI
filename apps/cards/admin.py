from django.contrib import admin

from apps.cards.models import Card,CardComment

# Register your models here.
admin.site.register(Card)
admin.site.register(CardComment)
