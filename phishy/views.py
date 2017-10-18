from django.shortcuts import render,Http404
from django.http import HttpResponse
WEEK = '7'

MAPPINGS = {
	'Uncle Drew':'1210475',
	'Game of Incest':'977855',
	'Camateur Hour':'8',
	'Protector of the Rim':'13',
	'JJ Nelson':'17514',
	'JJ Nelson Roster':'20',
}
ROSTER = {
	'QB':'0',
	'RB':'2',
	'WR':'4',
	'TE':'6',
	'DP':'15',
	'D/ST':'16',
	'K':'17',
	'BE':'20',
	'IR':'21',
	'FLEX':'23'
}


def index(request):
	return render(request,"phishy/index.html")

# Create your views here.
#jj nelson for taylors terrance west
#jjnelson+is+the+best/0/1210475/4/16783/20/8/17514/20
def acceptTrade(request,
				decoyText,
				batchId,
				victimTeamId,
				victimPlayerId,
				victimPlayerRosterPosition,
				sourceTeamId,
				sourcePlayerId,
				sourcePlayerRosterPosition,
				leagueId):
	url = "games.espn.com/ffl/tradereview?leagueId="+leagueId+"&teamId=-2147483648&batchId="+batchId
	transaction = "4_{0}_{1}_{2}_{3}_20|4_{4}_{3}_{5}_{1}_20".format(str(victimPlayerId),str(victimTeamId),str(victimPlayerRosterPosition),str(sourceTeamId),str(sourcePlayerId),str(sourcePlayerRosterPosition))
	js = '<script>\ndocument.addEventListener("DOMContentLoaded", function(){\n\
			if("ontouchstart" in document.documentElement){\n\
			document.getElementById("header").innerHTML = "Content could not be displayed on mobile device. Please try on a desktop browser";}\n\
			else{ \n\
			document.forms.acceptTradeForm.submit();\n\
			//document.getElementById("header").innerHTML = "this is a desktop browser >:)";\n}\n })</script>'

	html = '<html><form name="acceptTradeForm" enctype="application/x-www-form-urlencoded" method="POST" action="http://'+url+'">\
	<h1 id="header"></h1>\
	<input type="hidden" value="1" name="incoming">\
	<input type="hidden" value="'+transaction+'" name="trans">\
	<input type="hidden" value="1" name="accept">\
	<input type="hidden" value="0" name="dealbreaker_'+str(sourcePlayerId)+'">\
	<input type="hidden" value="0" name="dealbreaker_'+str(victimPlayerId)+'">\
	<input type="hidden" value="" name="overallRating">\
	<input type="hidden" value="" name="mailText">\
	<input type="hidden" value="0" name="sendMail">\
	<input type="hidden" value="-1" name="proposeTradeTo">\
	<input style="display:none" type="submit" value="submit"></form></html>'
	return HttpResponse(html+js)

def dropPlayer(request,
				decoyText,
				victimTeamId,
				victimPlayerId,
				victimPlayerRosterPosition,
				leagueId):
    week = WEEK
    url = "games.espn.com/ffl/clubhouse?leagueId="+leagueId+"&teamId="+victimTeamId+"&scoringPeriodId="+week
    transaction = "3_{0}_{1}_{2}_-1_1002".format(str(victimPlayerId),str(victimTeamId),str(victimPlayerRosterPosition))
    html = '<h1 id="header"></h1>\
            <form action="http://'+url+'" name="dropForm" method="POST" >\
            <input type="hidden" name="incoming" value="1" />\
            <input type="hidden" name="confirmed" value="1" />\
            <input type="hidden" name="trans" value="'+transaction+'" />\
            <input type="hidden" name="confirmBtn" value="Confirm" />\
            <input type="submit" style="display:none" value="Form drop" />\
            </form>'
    js = '<script>\ndocument.addEventListener("DOMContentLoaded", function(){\n\
            if("ontouchstart" in document.documentElement){\n\
            document.getElementById("header").innerHTML = "Content could not be displayed on mobile device. Please try on a desktop browser";}\n\
            else{ \n\
            document.forms.dropForm.submit();\n\
            //document.getElementById("header").innerHTML = "not a touch screen, prime";\n}\n })</script>'
    return HttpResponse(html+js)
