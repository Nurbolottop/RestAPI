from django.urls import path
from rest_framework.routers import DefaultRouter

#My imports
from apps.cards.views import CardAPI,CardSearchAPIView,CommentAPIViewSet

router = DefaultRouter()
router.register(prefix="cards", viewset= CardAPI, basename="cards")
router.register(prefix='comment', viewset=CommentAPIViewSet, basename="comment")

urlpatterns = [
    path('cards/search/', CardSearchAPIView.as_view(), name='search')
    
]
urlpatterns += router.urls
