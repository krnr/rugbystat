# -*- coding: utf-8
from django.shortcuts import render_to_response
from matches.models import Matches
#from django.http import HttpResponse
from django.db.models import Q

import datetime

# Create your views here.

def matches(request):
	return render_to_response('matches.html',
		{'matches': Matches.objects.all(),
		})

def team(request, team_name):

    double_names = {u'Волга': [u'Волгоград'],
        u'Герои': [u'Волга', u'Волгоград'],
        u'Волгоград': [u'Герои', u'Волга'],
        u'Парма': [u'Пермь', u'Витязь'],
        u'Пермь':  [u'Парма', u'Витязь'],
        u'Витязь':  [u'Парма', u'Пермь'],
        u'Гвозди': [u'Гвозди & Co'],
        u'МГОСГИ': [u'Феникс', u'Феникс (МГОСГИ)'],
        u'Феникс': [u'МГОСГИ', u'Феникс (МГОСГИ)'],
        u'Феникс (МГОСГИ)': [u'Феникс', u'МГОСГИ'],
        u'Гранит': [u'МИЭМ'],
        u'Адреналин': [u'Адреналин (Урал)'],
        u'Молот': [u'Молот-Тарханово'],
        u'Тарханово': [u'Молот-Тарханово'],
        u'ВВА': [u'Монино'],
        u'Монино': [u'ВВА'],
        u'МГТУ ГА': [u'МИИГА'],
        u'Зеленоград': [u'Доверие'],
        u'Доверие': [u'Зеленоград'],
        u'Орел': [u'Стальной Орел'],
        u'Стальной Орел': [u'Орел'],
        }

    if team_name in double_names.keys():
        sql = 'home = \'%s\' or away = \'%s\'' % (team_name, team_name)
        for team in double_names[team_name]:
            sql += ' or home = \'%s\' or away = \'%s\'' % (team, team)
        match_list = Matches.objects.extra(where = [sql]).order_by('-match_date')
    else:
        match_list = Matches.objects.filter(Q(home=team_name) | Q(away = team_name)).order_by('-match_date')
    print len(match_list), "<- length"
    return render_to_response('team.html',
		{'matches': match_list,
		'team': team_name,
		'teams': get_all_teams(),
		})

def get_all_teams():
    team_list = list(Matches.objects.order_by().values_list('home', flat=True).distinct())
    away_list = list(Matches.objects.order_by().values_list('away', flat=True).distinct())
    team_list += away_list
    team_list = sorted(set(team_list))
    return team_list

def teams(request):
    recent_matches = Matches.objects.filter(match_date__lte=datetime.datetime.today(), match_date__gt=datetime.datetime.today()-datetime.timedelta(days=30)).order_by('-match_date')
    total = Matches.objects.count()
    return render_to_response('teams.html',
		{'teams': get_all_teams(),
		'matches': recent_matches,
		'total': str(total)
		})

def tourn(request, tourn_name):
    tourn_list = Matches.objects.filter(Q(tournament=tourn_name)).order_by('-match_date')
    return render_to_response('tourn.html',
		{'matches': tourn_list,
		'tourn': tourn_name,
		'teams': get_all_teams(),
		})


def _404(request):
    return render_to_response('404.html',
    )
