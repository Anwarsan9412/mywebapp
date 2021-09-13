from django.db.models import fields
import django_filters
from django_filters import DateFilter
from django_filters.filters import CharFilter

from .models import Post

class PostFilter(django_filters.FilterSet):
    # start_date = DateFilter(field_name="data_created", lookup_expr='gte')
    # end_date = DateFilter(field_name="data_created", lookup_expr='lte')
    judul = CharFilter(label='Judul' ,field_name="judul", lookup_expr='icontains')
    body = CharFilter(label='Body', field_name="body", lookup_expr='icontains')
    class Meta:
        model = Post 
        fields = ['judul','body','category']
        # exclude = ['published','update','slug','author','username']
        