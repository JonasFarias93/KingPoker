from django.contrib import admin
from .models import Image

# Register your models here.
class ImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'public_id')
    search_fields = ('title',)

admin.site.register(Image, ImageAdmin)