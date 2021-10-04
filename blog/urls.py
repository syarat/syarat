from django.urls import path, re_path, register_converter
from datetime import datetime
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    re_path(r'^searchh?$', views.search_query, name='search_query'),
    # path('search' + query, views.search_query, name='search_query'),
    path('semua-syarat/', views.blog, name='blog'),
    path('categories/', views.categories, name='categories'),
    path('tags/', views.tags, name='tags'),
    path('<str:url>/', views.blog_details, name='blog_detail'),
    path('category/<str:category_url>/', views.category_details, name='category_details'),
    path('tag/<str:tag_url>/', views.tag_details, name='tag_details'),
    re_path(r'^apa-itu-syarat?', views.what, name='what'),
    path('contact', views.contact, name='contact')
]