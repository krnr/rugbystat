from django.contrib import admin
from matches.models import Match, Team
# Register your models here.

class MatchesAdmin(admin.ModelAdmin):
    search_fields = ['home', 'away']
    list_display = ('__str__', 'tournament', 'year', 
                    'home_rating_after', 'away_rating_after')
    list_filter = ('match_date', 'year')
    fieldsets = (
        ('Teams', {'fields':
            (('home', 'away'), ('home_link', 'away_link'))
        }),
        ('Score', {'fields':
            (('home_score', 'away_score'),)
        }),
        ('Rating', {'fields':
            (('home_rating_before', 'away_rating_before'),
            ('home_rating_after', 'away_rating_after'))
        }),
        ('Match', {'fields':
            ('match_date',
            ('tournament', 'stadium', 'ref'))
        }),
        ('Scorers', {'fields':
            (('home_scorers', 'away_scorers'))
        }),
        (None, {'fields':
            ('comment', 'doubtdate')
        }),
    )
    
    def year(self, obj):
        return obj.match_date.strftime('%Y')
    year.admin_order_field = 'match_date'
    year.short_description = 'Year'


class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'link', 'in_menu', )
    list_filter = ('city', 'in_menu')


admin.site.register(Match, MatchesAdmin)
admin.site.register(Team, TeamAdmin)