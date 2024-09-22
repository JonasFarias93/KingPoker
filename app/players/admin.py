from django.contrib import admin
from players.models import Participant

class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('name','points','is_member', 'count_for_ranking', 'city')
    search_fields = ('name','city')

admin.site.register(Participant, ParticipantAdmin)