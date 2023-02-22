from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from apps.cards.models import Manga
from apps.cards.serializers import MangaSerializers

# Create your views here.
class MangaAPI(ListCreateAPIView):
    queryset = Manga.objects.all() 
    serializer_class = MangaSerializers

class MangaDetailAPI(RetrieveUpdateDestroyAPIView):
    queryset = Manga.objects.all()
    serializer_class = MangaSerializers
