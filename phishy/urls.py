from django.conf.urls import url,include
from django.contrib.auth import views as auth_views


from . import views
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^ffl/(?P<decoyText>[0-9a-z+]+)/(?P<batchId>[0-9]+)/(?P<victimTeamId>[0-9]+)/(?P<victimPlayerId>[0-9]+)/(?P<victimPlayerRosterPosition>[0-9]+)/(?P<sourceTeamId>[0-9]+)/(?P<sourcePlayerId>[0-9]+)/(?P<sourcePlayerRosterPosition>[0-9]+)/(?P<leagueId>[0-9]+)/$',views.acceptTrade,name='ffl'),

]