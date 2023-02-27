#Rest
from rest_framework import serializers

#My imports
from .models import Card,CardComment


#CommentSerializer
class CardCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CardComment
        fields = "__all__"

#CardSerializer
class CardSerializers(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields =('id','user','title','type',
                 'years', 'genres','descriptions'
                 )
                  
class CardDetailSerializers(serializers.ModelSerializer):
    card_comments = CardCommentSerializer(read_only = True, many = True)
    class Meta:
        model = Card
        fields =('id','user','title','type',
                 'years', 'genres','descriptions','card_comments'
                 )
