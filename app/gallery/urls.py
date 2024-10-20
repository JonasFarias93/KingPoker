from django.urls import path
from . import views

urlpatterns = [
    path('', views.gallery_views, name='gallery_list'),
    path('gallery/delete/<int:image_id>/', views.delete_image, name='delete_image'),
]
