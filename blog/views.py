from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.core.paginator import Paginator
from django.contrib import messages
from .models import Blog, Category, Tag
from search.search import Search


def home(request):
    i = Blog.objects.filter(action='Publish').order_by('-updated')

    x = {
        'i': i,
    }
    return render(request, 'shared/home.html', x)


def search_query(request):
    search = Search(request.GET, queryset=Blog.objects.filter(action='Publish'))
    return render(request, 'shared/result.html', {'search': search})


def blog(request):
    i = Blog.objects.filter(action='Publish').order_by('-updated')

    paginator = Paginator(i, 5)
    page_number = request.GET.get('page')
    obj = paginator.get_page(page_number)

    x = {
        'i': i,
        'obj': obj
    }
    return render(request, 'blog/blog.html', x)


def blog_details(request, url):
    i = get_object_or_404(Blog, url=url)
    t = i.tag.all()

    x = {
        'i': i,
        't': t
    }
    return render(request, 'blog/details.html', x)


def categories(request):
    i = Category.objects.all()

    x = {
        'i': i
    }
    return render(request, 'shared/categories.html', x)


def category_details(request, category_url):
    i = Category.objects.get(category_url=category_url)
    c = Blog.objects.filter(category__in=Category.objects.filter(category_name=i))

    x = {
        'i': i,
        'c': c
    }
    return render(request, 'shared/cat_detail.html', x)


def tags(request):
    i = Tag.objects.all()

    x = {
        'i': i
    }
    return render(request, 'shared/tags.html', x)


def tag_details(request, tag_url):
    i = Tag.objects.get(tag_url=tag_url)
    i_tag = Blog.objects.filter(tag__in=Tag.objects.filter(tag_url=i))
    x = {
        'i': i,
        'i_tag': i_tag
    }
    return render(request, 'shared/t_details.html', x)


def what(request):
    return render(request, 'shared/what.html')


def contact(request):
    return render(request, 'shared/contact.html')
