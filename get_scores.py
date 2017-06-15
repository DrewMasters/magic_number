import urllib2
from bs4 import BeautifulSoup

url = raw_input("url: ")

page = urllib2.urlopen(url)

soup = BeautifulSoup(page)

scores = soup.find('div', id='scoreboardMatchups').findAll('table',{"class" : "ptsBased matchup"})


for game in scores:
	teams = game.findAll('tr')
	for t in teams:
		team = t.find('a')
		name = t.find('span',{"class" : "owners"})
		score = t.find('td',{"class" : "score"})
		if team != None:
			print str(team.contents[0].encode("ascii")) + " " + str(name.contents[0].encode("ascii")) + " " + str(score.contents[0].encode("ascii"))
	print
