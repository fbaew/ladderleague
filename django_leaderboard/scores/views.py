from django.shortcuts import render
from django.http import HttpResponse
from scores.models import Player, Game, Set
from django.template import RequestContext, loader

# Create your views here.

def leaders(request):
    player_list = Player.objects.all()
    template = loader.get_template('scores/index.html')
    context = RequestContext(request, {
        'players':player_list,
    })
    return HttpResponse(template.render(context))
