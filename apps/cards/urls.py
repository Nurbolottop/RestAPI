from django.urls import path
from rest_framework.routers import DefaultRouter

#My imports
from apps.cards.views import CardAPI,CardDetailAPI,CardSearchAPIView,CommentAPIViewSet

router = DefaultRouter()
router.register(prefix='comment', viewset=CommentAPIViewSet)
urlpatterns = [
    path('api/card/', CardAPI.as_view(), name="api_Card"),
    path('api/card/<int:pk>', CardDetailAPI.as_view(), name="api_card"),
    path('api/card/search/', CardSearchAPIView.as_view(), name='search'),
    
]
urlpatterns += router.urls
