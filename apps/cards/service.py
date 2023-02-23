#Django
from django_filters import rest_framework as filters

#My imports
from .models import Card

#Filters
class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass

class CardFilter(filters.FilterSet):
    genres = CharFilterInFilter(field_name='genres', lookup_expr='in')
    
    class Meta:
        model = Card
        fields = ['genres']