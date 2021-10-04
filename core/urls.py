from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.sitemaps.views import sitemap


from blog.sitemaps import BlogSiteMap, CategorySiteMap, TagSiteMap

sitemaps = {
    'article': BlogSiteMap,
    'category': CategorySiteMap,
    'tag': TagSiteMap
}


urlpatterns = [
    path('syarat_sitemaps.xml', sitemap, {'sitemaps': sitemaps}, name='syarat_sitemaps'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()


