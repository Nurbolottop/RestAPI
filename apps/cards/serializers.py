#Rest
from rest_framework import serializers
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin, DestroyModelMixin
#My imports
from .models import Card,CardComment
#CardSerializer
class CardSerializers(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ('id', 'title', 'type', 
                  'years', 'genres','descriptions'
                  )

#CommentSerializer
class CardCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CardComment
        fields = "__all__"

