from django.contrib import admin
from matches.models import Match, Team
# Register your models here.

class MatchesAdmin(admin.ModelAdmin):
    search_fields = ['home','away']
    #list_display = ['home','away', 'match_date']
    list_filter = ('match_date',)

admin.site.register(Match, MatchesAdmin)
admin.site.register(Team)