from django.contrib import admin
from .models import Category, Tag, Blog


admin.site.site_header = "Syarat Dashboard"
admin.site.site_title = "Syarat"
admin.site.index_title = "Syarat"


class CategoryAdmin(admin.ModelAdmin):
    pass


class TagAdmin(admin.ModelAdmin):
    pass


class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'action', 'created', 'updated']


admin.site.register(Tag, TagAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Blog, BlogAdmin)

