# -*- coding: utf-8
from django.shortcuts import render_to_response
from matches.models import Matches, Team
#from django.http import HttpResponse
from django.db.models import Q

import datetime, operator

# Create your views here.

def matches(request):
    return render_to_response('matches.html',
        {'matches': Matches.objects.all(),
        })

def get_all_teams():
    return list(Team.objects.filter(in_menu=True))

def get_match_list(team_name):
    '''
    team_name is field "latin" in a Team object
    '''
    double_names = {
        'geroi': ['geroi', 'volgograd'],
        'volgograd': ['volgograd', 'geroi', 'volga'],
        'molot': ['molot-tarhanovo', 'molot'],
        'tarhanovo': ['tarhanovo', 'molot-tarhanovo'],
        'granit': ['granit-gvozdi', 'granit'],
        'gvozdi': ['granit-gvozdi', 'gvozdi'],
        'belaya_krepost': ['belgorod-orel', 'belaya_krepost'],
        'orel': ['orel', 'belgorod-orel'],
        }
    if team_name in double_names.keys():
        return Matches.objects.filter(Q(home_link__latin__in=list(double_names[team_name])) | Q(away_link__latin__in=list(double_names[team_name])))
    else:
        return Matches.objects.filter(Q(home_link__latin=team_name) | Q(away_link__latin = team_name))

def matches_by_year(match_list):
    '''
    match_list is a parameter - querylist result after get_match_list() function.
    returns a list of lists in a format [[year, _all_matches_from_the_year], [...]]
    '''
    # get all dates, result is a list of tuples
    dates_list = match_list.values_list('match_date')
    # start an empty list of years to get and empty final dict
    years, match_by_year = list(), list()
    # iterate tuples
    for entry in dates_list:
        if entry[0].year not in years:
            years.append(entry[0].year)
    # now populate final list from the 'years' list: [year, list_of_matches]
    for year in years:
        match_by_year.append([year, match_list.filter(match_date__year=year)])
    return match_by_year

def get_rating(team_name, match_list):
    '''
    team_name is field "latin" in a Team object
    match_list is a querylist result after get_match_list() function
    '''
    if team_name == match_list[0].home_link.latin:
        return match_list[0].home_rating_after
    else:
        return match_list[0].away_rating_after

def team(request, team_name):
    '''
    team_name is a field "latin" in a Team object
    match_list is a querylist result after get_match_list() function
    '''
    match_list = get_match_list(team_name)
    rating = get_rating(team_name, match_list)
    return render_to_response('team.html',
        {'matches': matches_by_year(match_list),
        'team': Team.objects.filter(latin=team_name)[0],
        'teams': get_all_teams(),
        'rating': rating
        })

def teams(request):
    recent_matches = Matches.objects.filter(match_date__lte=datetime.datetime.today(), match_date__gt=datetime.datetime.today()-datetime.timedelta(days=30))
    total = Matches.objects.count()
    return render_to_response('teams.html',
        {'teams': get_all_teams(),
        'matches': recent_matches,
        'total': str(total)
        })

def tourn(request, tourn_name):
    tourn_list = Matches.objects.filter(Q(tournament=tourn_name))
    return render_to_response('tourn.html',
        {'matches': matches_by_year(tourn_list),
        'tourn': tourn_name,
        'teams': get_all_teams(),
        })

def _404(request):
    teams, rating = get_all_teams(), {}
    # make a dict with the pairs 'team-rating'
    for t in teams:
        rating[t.name] = get_rating(t.latin, get_match_list(t.latin))
    rating_sort = sorted(rating.items(), key=operator.itemgetter(1), reverse=True)
    return render_to_response('404.html',
    {'teams': teams,
    'rating': rating_sort
    })

def handler500(request):
    response = render_to_response('500.html',
    {'teams': get_all_teams(),
    })
    return response