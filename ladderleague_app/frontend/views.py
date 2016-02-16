from django.http import HttpResponse
from django.template import loader
from django.db.models import Q
from scores.models import Player, Game, Contest

# Create your views here.


def _leaderboard_html(request):
    all_players = Player.objects.order_by("-ladder_rank")
    leaderboard_template = loader.get_template('frontend/leaders.html')
    leaderboard_html = leaderboard_template.render(
        {'leaders': all_players},
        request
    )
    return leaderboard_html


def _player_summary(request, player_name):
    """
    Subview showing the player's details:
        Profile pic
        Overall record
        Set History
    """

    contest_list = Contest.objects.filter(
        Q(challenger=Player.objects.get(short_id=player_name.upper())) |
        Q(challengee=Player.objects.get(short_id=player_name.upper()))
    ).order_by('id')

    results = [{
        'contest': x,
        'outcome': x.outcome(Player.objects.get(short_id=player_name.upper()))
    } for x in contest_list]

    wins = 0
    for result in results:
        if result["outcome"] == "win":
            wins += 1
    player = Player.objects.get(short_id=player_name.upper())

    standings = Player.objects.order_by("-ladder_rank")
    ranking = list(standings).index(player) + 1

    player = Player.objects.get(short_id=player_name.upper())
    profile_template = loader.get_template('frontend/player.html')
    profile_html = profile_template.render(
        {
            'all_contests': contest_list,
            'results': results,
            'player': player,
            'ranking': ranking,
            'wins': wins,
        },
        request
    )
    return profile_html


def _contest_summary_html(request, requested_contest):
    contest_summary_template = loader.get_template('frontend/contest.html')
    contest_summary_html = contest_summary_template.render(
        {
            'contest': requested_contest,
            'games': requested_contest.game_set.all()
        },
        request
    )
    return contest_summary_html


def index(request):
    """
    Main index view; This will be the main landing page.
    :param request The HttpRequest that prompted this view to be rendered.

    """
    master_template = loader.get_template('frontend/index.html')
    html = master_template.render(
        {
            'leaders': _leaderboard_html(request),
        },
        request
    )
    return HttpResponse(html)


def player_overview(request, player_name):
    if Player.objects.filter(short_id=player_name.upper()).exists():
        master_template = loader.get_template('frontend/index.html')
        master_html = master_template.render(
            {
                'leaders': _leaderboard_html(request),
                'profile': _player_summary(request, player_name)
            },
            request
        )
        return HttpResponse(master_html)
    else:
        return HttpResponse("Sorry, no such player")


def contest_overview(request, player_name, contest_number):
    """
    Show the details of a given contest involving player_name

    :param request The HttpRequest that prompted this view to be rendered.

    :param  player_name The shortid (case-insensitive) of the player whose
            profile we are looking at.
    :param  contest_number The id number of the Contest we will display.
    """
    player_exists = False
    contest_exists = False
    if Player.objects.filter(short_id=player_name.upper()).exists():
        player_exists = True
    if Contest.objects.filter(id=contest_number).exists():
        contest_exists = True

    if not player_exists or not contest_exists:
        return HttpResponse("invalid player/set combination")
    requested_contest = Contest.objects.filter(id=contest_number)[0]
    player = Player.objects.filter(short_id=player_name.upper())[0]

    if not (
        requested_contest.challenger == player or
        requested_contest.challengee == player
    ):
        return HttpResponse(
            "That player did not play in that set. {}".format(
               requested_contest
            )
        )
    else:
        master_template = loader.get_template('frontend/index.html')
        master_html = master_template.render(
            {
                'leaders': _leaderboard_html(request),
                'profile': _player_summary(request, player_name),
                'contest_details': _contest_summary_html(
                    request, requested_contest
                )
            },
            request
        )
        return HttpResponse(master_html)
