from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView

from apps.cards.models import Manga
from apps.cards.serializers import MangraSerializers

# Create your views here.
class MangaAPI(ListCreateAPIView):
    queryset = Manga.objects.all() 
    serializers_class = MangraSerializers

    