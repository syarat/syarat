import django_filters
from django import forms
from blog.models import Blog


class Search(django_filters.FilterSet):

    q = django_filters.CharFilter(
        field_name='article',
        lookup_expr='icontains',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control search',
                'placeholder': 'Search'
            }
        )
    )

    class Meta:
        model = Blog
        fields = ['title', 'article']