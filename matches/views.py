# -*- coding: utf-8
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.db.models import Q
from matches.models import Match, Team
from matches.forms import MatchForm

import datetime, operator, json

# Create your views here.

def matches(request):
    '''
    test view which renders ALL database
    '''
    return render_to_response('matches.html',
        {'matches': Match.objects.all(),
        })

def get_all_teams():
    return Team.objects.filter(in_menu=True)

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
        return Match.objects.filter(Q(home_link__latin__in=list(double_names[team_name])) | Q(away_link__latin__in=list(double_names[team_name]))).extra({'year': 'extract(year from match_date)'})
    else:
        return Match.objects.filter(Q(home_link__latin=team_name) | Q(away_link__latin = team_name)).extra({'year': 'extract(year from match_date)'})

def get_rating(team_name):
    '''
    team_name is field "latin" in a Team object
    match_list is a querylist result after get_match_list() function
    '''
    match_list = get_match_list(team_name)
    try:
        # home Team is a 'rating' team and we can check if it is a team_name
        if team_name == match_list[0].home_link.latin:
            return match_list[0].home_rating_after
        else:
            return match_list[0].away_rating_after
    except AttributeError as e:
        print e
        # home Team is non-rating, so check only away team:
        if match_list[0].away_link.latin and team_name == match_list[0].away_link.latin:
            return match_list[0].away_rating_after
        else:
            # somehow both team has no 'latin' field. it's an error
            print "check 'latin' fields of the team %s" % team_name
            return 0

def team(request, team_name):
    '''
    team_name is a field "latin" in a Team object
    '''
    match_list = get_match_list(team_name)
    team_rating = get_rating(team_name)
    return render_to_response('team.html',
        {'matches': match_list,
        'team': Team.objects.filter(latin=team_name)[0],
        'teams': get_all_teams(),
        'rating': team_rating
        })

def teams(request):
    '''
    returns mainpage
    '''
    recent_matches = Match.objects.filter(match_date__lte=datetime.datetime.today(), 
                                          match_date__gt=datetime.datetime.today() - datetime.timedelta(days=30))
    total = Match.objects.count()
    teams = get_all_teams()
    return render_to_response('teams.html',
        {'teams_left': teams[:(len(teams) / 10) * 7],
        'teams_right': teams[(len(teams) / 10) * 7:],
        'matches': recent_matches,
        'total': str(total)
        })

def old_teams(request):
    recent_matches = Match.objects.filter(match_date__lte=datetime.datetime.today(), 
                                          match_date__gt=datetime.datetime.today() - datetime.timedelta(days=30))
    total = Match.objects.count()
    teams = Team.objects.filter(in_menu=False)

    return render_to_response('teams.html', {
        'teams_left': teams[:(len(teams) / 10) * 7],
        'teams_right': teams[(len(teams) / 10) * 7:],
        'matches': recent_matches,
        'total': str(total)
    })

def tourn(request, tourn_name):
    '''
    returns all matches of a tournament given by name in unicode
    i.e. 'ПФО-Север' for http://..../tourn/ПФО-Север/
    '''
    tourn_list = Match.objects.filter(Q(tournament=tourn_name)).extra({'year': 'extract(year from match_date)'})
    return render_to_response('tourn.html',
        {'matches': tourn_list,
        'tourn': tourn_name,
        'teams': get_all_teams(),
        })

def tourns(request):
    all_tourns = Match.objects.order_by().values('tournament').distinct()
    tourn_list = [el['tournament'] for el in all_tourns]
    tourn_list.sort()
    return render_to_response('all_tourn.html',
        {'tourns': tourn_list,
        'teams': get_all_teams(),
        })

def new_match(request):
    # first let's check AJAX requests
    if request.is_ajax():
        response_dict = {
            'success': True,
        }
        # AJAX must send us two int's - 'id_home' and 'id_away'
        id_home = request.POST.get('id_home')
        id_away = request.POST.get('id_away')
        # get Team objects and find theirs name and rating
        home = Team.objects.filter(id=id_home)[0]
        away = Team.objects.filter(id=id_away)[0]
        response_dict = {
            'home': home.name,
            'home_rating': str(get_rating(home.latin)),
            'away': away.name,
            'away_rating': str(get_rating(away.latin)),
        }
        # send back to the page
        return HttpResponse(json.dumps(response_dict), content_type="application/json"
)
    elif request.method == 'POST':
        form = MatchForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.comment += "\nAdded by the site form"
            post.save()
            print post
            return HttpResponseRedirect('/')
    else:
        form = MatchForm()
    return render_to_response('form.html',
        {'teams': get_all_teams(),
        'form': form
        }, context_instance=RequestContext(request))

def rating(request):
    teams, rating = get_all_teams(), {}
    # make a dict with the pairs 'team-rating'
    for t in teams:
        rating[t] = get_rating(t.latin)
    rating_sort = sorted(rating.items(), key=operator.itemgetter(1), reverse=True)
    return render_to_response('rating.html',
    {'teams': teams,
    'rating': rating_sort
    })

def _404(request):
    return render_to_response('404.html',
    {'teams': get_all_teams(),
    })

def handler500(request):
    response = render_to_response('500.html',
    {'teams': get_all_teams(),
    })
    return response