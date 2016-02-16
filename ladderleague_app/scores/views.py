from django.shortcuts import render

from django.http import HttpResponse
from scores.models import Player
from django.template import loader

# Create your views here.


def player_list(request):
    """
    List all players, plain and simple.

    :param request The HttpRequest that prompted this view to be rendered.
    """
    all_players = Player.objects.all()
    template = loader.get_template("scores/players.html")
    html = template.render({'players': all_players})
    return HttpResponse(html)
