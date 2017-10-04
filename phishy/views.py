from django.shortcuts import render
from django.http import HttpResponse

MAPPINGS = {
	'Uncle Drew':1210475,
	'Game of Incest':,
	'Camateur Hour':8,
	'Protector of the Rim':,
	'JJ Nelson':17514,
	'JJ Nelson Roster':20,
}

def index(request):
	return HttpResponse("Hello World.")

# Create your views here.
#jj nelson for taylors terrance west
#jjnelson+is+the+best/0/1210475/4/16783/20/8/17514/20
def acceptTrade(request,
				decoyText,
				batchId,
				victimTeamId,
				victimPlayerId,
				victimPlayerRosterPosition,
				sourceTeamId=MAPPINGS['Camateur Hour'],
				sourcePlayerId=MAPPINGS['JJ Nelson'],
				sourcePlayerRosterPosition=MAPPINGS['JJ Nelson Roster'],
				leagueId=MAPPINGS['Uncle Drew']):

    url = "games.espn.com/ffl/tradereview?leagueId="+leagueId+"&teamId=-2147483648&batchId=39"
    transaction = "4_{0}_{1}_{2}_{3}_20|4_{4}_{3}_{5}_{1}_20".format(str(victimPlayerId),str(victimTeamId),str(victimPlayerRosterPosition),str(sourceTeamId),str(sourcePlayerId),str(sourcePlayerRosterPosition))
    html = '<html><form enctype="application/x-www-form-urlencoded" method="POST" action="http://'+url+'"><table><tr><td>incoming</td><td><input type="text" value="1" name="incoming"></td></tr>\
<tr><td>trans</td><td><input type="hidden" value="'+transaction+'" name="trans"></td></tr>\
<tr><td>accept</td><td><input type="hidden" value="1" name="accept"></td></tr>\
<tr><td></td><td><input type="hidden" value="0" name="dealbreaker_'+str(sourcePlayerId)+'"></td></tr>\
<tr><td></td><td><input type="hidden" value="0" name="dealbreaker_'+str(victimPlayerId)+'"></td></tr>\
<tr><td>overallRating</td><td><input type="hidden" value="" name="overallRating"></td></tr>\
<tr><td>mailText</td><td><input type="hidden" value="" name="mailText"></td></tr>\
<tr><td>sendMail</td><td><input type="hidden" value="0" name="sendMail"></td></tr>\
<tr><td>proposeTradeTo</td><td><input type="hidden" value="-1" name="proposeTradeTo"></td></tr>\
</table><input type="submit" value="submit"></form></html>'
    return HttpResponse(html)

def dropPlayer(request,
				decoyText,
				victimTeamId,
				victimPlayerId,
				victimPlayerRosterPosition,
				week,
				leagueId=MAPPINGS['Uncle Drew']):
	url = "games.espn.com/ffl/clubhouse?leagueId="+leagueId+"&teamId="+victimTeamId+"&scoringPeriodId="+week
	html = '<form action="http://'+url+'" name="dropForm" method="POST" >\
      <input type="hidden" name="incoming" value="1" />\
      <input type="hidden" name="confirmed" value="1" />\
      <input type="hidden" name="trans" value="3&#95;13994&#95;20&#95;&#45;1&#95;1002" />\
      <input type="hidden" name="confirmBtn" value="Confirm" />\
      <input type="submit" value="Form drop" />\
    </form>'
    return HttpResponse(html)
