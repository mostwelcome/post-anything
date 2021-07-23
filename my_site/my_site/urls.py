from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from blog import urls as blog_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include(blog_urls, namespace='blog'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
