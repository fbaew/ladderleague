from django.shortcuts import render
from django.http import HttpResponse
from scores.models import Player, Game, Set
from django.template import RequestContext, loader
import random

# Create your views here.

# def leaders(request):
#     player_list = Player.objects.all()
#     template = loader.get_template('scores/index.html')
#     context = RequestContext(request, {
#         'players':player_list,
#     })
#     return HttpResponse(template.render(context))
# 
def leaders(request):
    player_list = Player.objects.all()
    template = loader.get_template('scores/leaders.html')

    return HttpResponse(template.render({
       'leaders':player_list,
       }, request))

def index(request):
    player_list = Player.objects.order_by("?") #performance; only temporary
    template = loader.get_template('scores/index.html')
    html = template.render({'leaders':player_list},request)
    return HttpResponse(html)

def player_summary(request,player_name):
    set_list_challenger = Set.objects.filter(
        player1= Player.objects.get(short_id=player_name)
    )

    set_list_challengee = Set.objects.filter(
        player2 = Player.objects.get(short_id=player_name)
    )
    template = loader.get_template('scores/player.html')
    html = template.render(
        {
            'challenger_sets':set_list_challenger,
            'challengee_sets':set_list_challengee,
        }
        , request
    )
    return HttpResponse(html)
