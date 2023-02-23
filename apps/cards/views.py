#rest
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import GenericViewSet
# from rest_framework.permissions import IsAuthenticated
from rest_framework.mixins import CreateModelMixin, DestroyModelMixin
from rest_framework import  pagination
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

#django
from django_filters.rest_framework import DjangoFilterBackend

#my imports
from .models import Card,CardComment
from .serializers import CardSerializers,CardCommentSerializer
from .service import CardFilter


#CardAPI
class CardAPI(ListCreateAPIView):
    class CardPagination(pagination.PageNumberPagination):
        page_size = 12
        
    queryset = Card.objects.all() 
    serializer_class = CardSerializers
    filter_backends = (DjangoFilterBackend,)
    filterset_class = CardFilter
    pagination_class = CardPagination

#CardDetailAPI
class CardDetailAPI(RetrieveUpdateDestroyAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializers
    
#CardSearchAPI
class CardSearchAPIView(APIView):
    def get(self, request, format=None):
        search_query = request.GET.get('search', '')
        cards = Card.objects.filter(title__icontains=search_query)
        serializer = CardSerializers(cards, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
#CardCommentAPI
class CommentAPIViewSet(GenericViewSet, CreateModelMixin,
                            DestroyModelMixin):
    queryset = CardComment.objects.all()
    serializer_class = CardCommentSerializer
    # permission_classes = (IsAuthenticated, )

    # def perform_create(self, serializer):
    #     return serializer.save(user = self.request.user)