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
    
    card_comments = CardCommentSerializer(read_only = True, many = True)
    count_comments = serializers.SerializerMethodField(read_only = True)
    
    class Meta:
        model = Card
        fields = "__all__"
                  
    def get_count_comments(self, instance):
        return instance.card_comments.all().count()



