"""
Views for scoreboard app
"""
from django.shortcuts import render
from django.http import HttpResponse
from scores.models import Player, Game, Set
from django.template import loader
from django.db.models import Q

# Create your views here.

def _player_summary(request, player_name):
    """
    Subview showing the player's details:
        Profile pic
        Overall record
        Set History
    """

    set_list = Set.objects.filter(
        Q(player1=Player.objects.get(short_id=player_name.upper())) |
        Q(player2=Player.objects.get(short_id=player_name.upper()))
    ).order_by('set_id')

    results = [{}]
    player = Player.objects.get(short_id=player_name.upper())

    player = Player.objects.get(short_id=player_name.upper())
    profile_template = loader.get_template('scores/player.html')
    profile_html = profile_template.render(
        {
            'all_sets':set_list,
            'results':results,
            'player':player,
        }
        , request
    )
    return profile_html

def _leaderboard_html(request):
    all_players = Player.objects.order_by("-elo_rating")
    leaderboard_template = loader.get_template('scores/leaders.html')
    leaderboard_html = leaderboard_template.render(
        {'leaders':all_players},
        request
    )
    return leaderboard_html

def _set_summary_html(request, requested_set):
    set_summary_template = loader.get_template('scores/set.html')
    set_summary_html = set_summary_template.render(
        {
            'single_set':requested_set,
            'games':requested_set.game_set.all()
        },
        request
    )
    return set_summary_html


def index(request):
    """
    Main index view; This will be the main landing page.
    """
    all_players = Player.objects.order_by("-elo_rating")

    master_template = loader.get_template('scores/landing.html')
    html = master_template.render(
        {
            'leaders':_leaderboard_html(request),
        },
        request
    )
    return HttpResponse(html)


def player_overview(request, player_name):
    if Player.objects.filter(short_id=player_name.upper()).exists():
        master_template = loader.get_template('scores/landing.html')
        master_html = master_template.render(
            {
                'leaders':_leaderboard_html(request),
                'profile':_player_summary(request, player_name)
            },
            request
        )
        return HttpResponse(master_html)
    else:
        return HttpResponse("Sorry, no such player")

def set_overview(request, player_name, set_number):
    """
    Show the details of a given set involving player_name
    """
    player_exists = False
    set_exists = False
    if Player.objects.filter(short_id=player_name.upper()).exists():
        player_exists = True
    if Set.objects.filter(set_id=set_number).exists():
        set_exists = True

    if not player_exists or not set_exists:
        return HttpResponse("invalid player/set combination")
    requested_set = Set.objects.filter(set_id=set_number)[0]
    player = Player.objects.filter(short_id=player_name.upper())[0]

    if not (requested_set.player1 == player or requested_set.player2 == player):
        return HttpResponse("That player is not in that set. {}".format(requested_set))
    else:
        master_template = loader.get_template('scores/landing.html')
        master_html = master_template.render(
            {
                'leaders':_leaderboard_html(request),
                'profile':_player_summary(request,player_name),
                'single_set':_set_summary_html(request, requested_set)
            },
            request
        )
        return HttpResponse(master_html)
