from django.contrib import admin
from django.urls import path, include

from .views import home

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('user/', include('user.urls')),
    path('book/', include('filtering.urls')),
    path('learning/', include('learning.urls')),
]
