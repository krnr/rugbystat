from django.contrib import admin
from matches.models import Matches, Team
# Register your models here.

class MatchesAdmin(admin.ModelAdmin):
    search_fields = ['home','away']
    #list_display = ['home','away', 'match_date']
    list_filter = ('match_date',)

admin.site.register(Matches, MatchesAdmin)
admin.site.register(Team)