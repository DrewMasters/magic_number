f = open('c_week', 'r')
s = open('standings', 'r')

standings = {}

for line in s:
	c = 0
	team = ""
	w = 0
	l = 0
	gr = 0
	for word in line.split():
		if c==0:
			team = str(word)
		elif c==1:
			w = int(word)
		elif c==2:
			l = int(word)
		elif c==3:
			gr = int(word)
		c=c+1
	standings[team] = [w,l,gr]

print standings

for line in f:
	c=0
	team1 = ""
	s1 = 0
	team2 = ""
	s2 = 0
	for word in line.split(" "):
		if c==0:
			team1 = str(word)
		elif c==1:
			s1 = int(word)
		elif c==2:
			team2 = str(word)
		elif c==3:
			s2 = int(word)
		c=c+1
	if s1 > s2:
		standings[team1][0] = int(standings[team1][0]) + 1
		standings[team2][1] = int(standings[team2][1]) + 1
	elif s1 < s2:
		standings[team1][1] = int(standings[team1][1]) + 1
		standings[team2][0] = int(standings[team2][0]) + 1
	standings[team1][2] = int(standings[team1][2]) - 1
	standings[team2][2] = int(standings[team2][2]) - 1

print standings
