from django.contrib import admin
from django.urls import path, include
from players.views import players_views, index_views
from gallery.views import  gallery_views, delete_image
from accounts.views import register_view
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', register_view, name='register'),
    path('players/', players_views, name='players_list'),
    path('gallery/', include('gallery.urls')), 
    path('', index_views)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
