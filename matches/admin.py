from django.contrib import admin
from matches.models import Match, Team
# Register your models here.

class MatchesAdmin(admin.ModelAdmin):
    search_fields = ['home','away']
    #list_display = ['home','away', 'match_date']
    list_filter = ('match_date',)
    fieldsets = (
        ('Teams', {'fields':
            (('home', 'away'), ('home_link', 'away_link'))
        }),
        ('Score', {'fields':
            (('home_score', 'away_score'),)
        }),
        ('Rating', {'fields':
            (('home_rating_before','away_rating_before'),
            ('home_rating_after','away_rating_after'))
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

admin.site.register(Match, MatchesAdmin)
admin.site.register(Team)