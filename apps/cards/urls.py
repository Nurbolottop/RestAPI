from django.urls import path

from apps.cards.views import MangaAPI

urlpatterns = [
    path('api/manga/', MangaAPI.as_view(), name="api_manga")
]