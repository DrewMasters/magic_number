import pandas as pd

file_location = r'./test_files/'
c_standings = 'standings.csv'
c_week = 'c_week.csv'
Total_games = 8
cutoff = 2

standings = pd.read_csv(file_location+c_standings,names=['Team','Wins','Losses','Games_Remaining','Magic_Number','Playoff_Magic_Number'])

standings['Team'] = standings['Team'].astype('str')

scores = open(file_location+c_week,'r')
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
		standings.loc[standings['Team']==team1,'Wins'] += 1
		standings.loc[standings['Team']==team2,'Losses'] += 1
	elif s1<s2:
		standings.loc[standings['Team']==team2,'Wins'] += 1
		standings.loc[standings['Team']==team1,'Losses'] += 1
	standings.loc[standings['Team']==team1,'Games_Remaining'] -= 1
	standings.loc[standings['Team']==team2,'Games_Remaining'] -= 1

Sort_standings = standings.sort_values(['Wins'],ascending=False)

top_team = Sort_standings.iloc[0].Wins
playoff_cutoff = Sort_standings.iloc[cutoff].Wins

Sort_standings.Magic_Number = Total_games + 1 - top_team - Sort_standings.Losses
Sort_standings.Playoff_Magic_Number = Total_games + 1 - playoff_cutoff - Sort_standings.Losses
