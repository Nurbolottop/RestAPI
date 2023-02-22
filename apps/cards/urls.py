from django.urls import path

from apps.cards.views import MangaAPI,MangaDetailAPI

urlpatterns = [
    path('api/manga/', MangaAPI.as_view(), name="api_manga"),
    path('api/manga/<int:pk>', MangaDetailAPI.as_view(), name="api_manga"),
    
]