import pandas as pd

c_standings = 'standings'
c_week = 'c_week'
Total_games = 6
cutoff = 2

standings = pd.read_csv(c_standings,names=['Team','W','L','GR','MN','PMN'])

standings['Team'] = standings['Team'].astype('str')

scores = open(c_week,'r')
for line in scores:
	c=0
	team1 = ""
	s1 = 0
	team2 = ""
	s2 = 0
	for word in line.split(","):
		if c==0:
			team1 = str(word)
		elif c==1:
			s1 = int(word)
		elif c==2:
			team2 = str(word)
		elif c==3:
			s2 = int(word)
		c=c+1
	if s1>s2:
		standings.loc[standings['Team']==team1,'W'] += 1
		standings.loc[standings['Team']==team2,'L'] += 1
	elif s1<s2:
		standings.loc[standings['Team']==team2,'W'] += 1
		standings.loc[standings['Team']==team1,'L'] += 1
	standings.loc[standings['Team']==team1,'GR'] -= 1
	standings.loc[standings['Team']==team2,'GR'] -= 1

Sort_standings = standings.sort_values(['W'],ascending=False)

top_team = Sort_standings.iloc[0].W
playoff_cutoff = Sort_standings.iloc[cutoff].W

Sort_standings.MN = Total_games + 1 - top_team - Sort_standings.L
Sort_standings.PMN = Total_games + 1 - playoff_cutoff - Sort_standings.L

Sort_standings.to_html('result.html',header=True,index=False)

Sort_standings.to_csv('result.csv',header=False,index=False)
