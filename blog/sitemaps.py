from django.contrib.sitemaps import Sitemap
from .models import Blog, Category, Tag


class BlogSiteMap(Sitemap):
    changefreq = 'daily'
    priority = 0.8

    def items(self):
        x = Blog.objects.all()
        return x

    def location(self, obj):
        return '/' + str(obj)


class CategorySiteMap(Sitemap):
    changefreq = 'daily'
    priority = 0.8

    def items(self):
        x = Category.objects.all()
        return x

    def location(self, obj):
        return '/category/' + str(obj)


class TagSiteMap(Sitemap):
    changefreq = 'daily'
    priority = 0.8

    def items(self):
        x = Tag.objects.all()
        return x

    def location(self, obj):
        return '/tag/' + str(obj)