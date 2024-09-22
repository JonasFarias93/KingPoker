from django.contrib import admin
from tournaments.models import *

class TornamentAdmin(admin.ModelAdmin):
    list_display = ('year','name_tornament')
    search_fields = ('name','city')

admin.site.register(Tornament, TornamentAdmin)

class RoundAdmin(admin.ModelAdmin):
    list_display = ('tornament', 'number', 'date','extra')
    search_fields = ('tornament', 'date')

admin.site.register(Round, RoundAdmin)

class ParticipantRoundAdmin(admin.ModelAdmin):
    list_display = ('round','participant','points','position')
    search_fields = ('round', 'participant')

admin.site.register(ParticipantRound, ParticipantRoundAdmin)

class FinalRankingAdmin(admin.ModelAdmin):
    list_display = ('tornament','participant','points','position')
    search_fields = ('tornament', 'participant')

admin.site.register(FinalRanking, FinalRankingAdmin)

class NivelBlindAdmin(admin.ModelAdmin):
    list_display = ('tornament','number','small_blind','big_blind','duration')
    search_fields = ('tornament')

class ArenaAdmin(admin.ModelAdmin):
    list_display = ('id','name','adress','city','description')
    search_fields = ('name','city')