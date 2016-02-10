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
