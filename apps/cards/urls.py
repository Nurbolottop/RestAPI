from django.urls import path
from rest_framework.routers import DefaultRouter

#My imports
from apps.cards.views import CardAPI,CardSearchAPIView,CommentAPIViewSet

router = DefaultRouter()
router.register(prefix="cards", viewset= CardAPI, basename="cards")

urlpatterns = [
    path('cards/search/', CardSearchAPIView.as_view(), name='search'),
    path('cards/comment/', CommentAPIViewSet.as_view(), name='comment'),
    
    
]
urlpatterns += router.urls
