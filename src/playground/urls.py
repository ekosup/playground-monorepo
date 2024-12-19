from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from .views import home, test_storage_connection

urlpatterns = [
    path('', home, name='home'),
    path('test-files/', test_storage_connection, name='test-files'),
    path('admin/', admin.site.urls),
    path('user/', include('user.urls')),
    path('book/', include('filtering.urls')),
    path('learning/', include('learning.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
