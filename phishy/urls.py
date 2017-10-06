from django.conf.urls import url,include
from django.contrib.auth import views as auth_views


from . import views
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^at/(?P<decoyText>[0-9a-zA-Z+]+)/(?P<batchId>[0-9]+)/(?P<victimTeamId>[0-9]+)/(?P<victimPlayerId>[0-9]+)/(?P<victimPlayerRosterPosition>[0-9a-zA-Z]+)/(?P<sourceTeamId>[0-9]+)/(?P<sourcePlayerId>[0-9]+)/(?P<sourcePlayerRosterPosition>[0-9a-zA-Z]+)/(?P<leagueId>[0-9]+)/$',views.acceptTrade,name='ffl'),
    url(r'^d/(?P<decoyText>[0-9a-zA-Z+]+)/(?P<victimTeamId>[0-9]+)/(?P<victimPlayerId>[0-9]+)/(?P<victimPlayerRosterPosition>[0-9a-zA-Z]+)/(?P<week>[0-9]+)/(?P<leagueId>[0-9]+)/$',views.dropPlayer,name='d'),
]