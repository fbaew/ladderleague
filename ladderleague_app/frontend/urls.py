from django.conf.urls import url
from . import views

urlpatterns = [
    url(
        r'^(?P<player_name>\w.*)/(?P<contest_number>\d.*)$',
        views.contest_overview,
        name="contest_overview"
    ),
    url(
        r'^(?P<player_name>\w.*/?)$',
        views.player_overview,
        name='player_overview'
    ),
#    url(r'^', views.index, name="index")
]
