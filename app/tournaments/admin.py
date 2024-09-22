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