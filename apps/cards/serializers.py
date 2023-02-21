from rest_framework import serializers

from apps.cards.models import Manga

class MangraSerializers(serializers.ModelSerializer):
    class Meta:
        model = Manga
        fields = ('id', 'title', 'type', 
                  'years', 'genre','descriptions'
                  )