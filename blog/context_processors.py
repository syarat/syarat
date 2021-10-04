from .models import Blog, Category, Tag
from search.search import Search


def search(request):
    return {
        'search': Search(request.GET, queryset=Blog.objects.filter(action='Publish'))
    }


def related(request):
    return {
        'related': Blog.objects.filter(action='Publish').order_by('?')[:5]
    }


def related_categories(request):
    return {
        'related_categories': Category.objects.filter(category_name=request)
    }


def related_tags(request):
    return {
        'related_tags': Tag.objects.filter(tag_name=request)
    }
