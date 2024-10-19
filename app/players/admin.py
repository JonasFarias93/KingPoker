from django.contrib import admin
from players.models import Participant
from .models import Image

class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('name','points','is_member', 'count_for_ranking', 'city')
    search_fields = ('name','city')

admin.site.register(Participant, ParticipantAdmin)

class ImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'public_id')
    search_fields = ('title',)

admin.site.register(Image, ImageAdmin)