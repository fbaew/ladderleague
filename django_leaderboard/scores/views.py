"""
Views for scoreboard app
"""
from django.shortcuts import render
from django.http import HttpResponse
from scores.models import Player, Game, Set
from django.template import loader
from django.db.models import Q

# Create your views here.

# def leaders(request):
#     player_list = Player.objects.all()
#     template = loader.get_template('scores/index.html')
#     context = RequestContext(request, {
#         'players':player_list,
#     })
#     return HttpResponse(template.render(context))
#
def index(request):
    """
    Main index view; This will be the main landing page.
    """
    all_players = Player.objects.order_by("-elo_rating")
    leaderboard_template = loader.get_template('scores/leaders.html')
    leaderboard_html = leaderboard_template.render(
        {'leaders':all_players},
        request
    )

    master_template = loader.get_template('scores/index.html')
    html = master_template.render(
        {'leaders':leaderboard_html,},
        request)
    return HttpResponse(html)

def player_summary(request, player_name):
    """
    Subview showing the player's details:
        Profile pic
        Overall record
        Set History
    """

    set_list = Set.objects.filter(
        Q(player1=Player.objects.get(short_id=player_name.upper())) |
        Q(player2=Player.objects.get(short_id=player_name.upper()))
    ).order_by('setid')

    results = [{}]

#    for single_set in set_list:
#        result = {}
#        result["outcome"] = "Draw"
#        player_ci = player_name.upper()
#        if single_set.winner() == Player.objects.get(short_id=player_ci):
#            result["outcome"] = "Win"
#        elif single_set.winner() == 

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

    all_players = Player.objects.order_by("-elo_rating")
    leaderboard_template = loader.get_template('scores/leaders.html')
    leaderboard_html = leaderboard_template.render(
        {'leaders':all_players},
        request
    )


    master_template = loader.get_template('scores/player_profile.html')
    master_html = master_template.render(
        {
            'leaders':leaderboard_html,
            'profile':profile_html
        },
        request
    )

    return HttpResponse(master_html)
