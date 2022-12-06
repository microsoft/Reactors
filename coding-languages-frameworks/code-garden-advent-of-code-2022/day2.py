
guide = [x.strip().split() for x in open("day2-data.txt").readlines()]

moveMapping = {
	"A": "R",
	"B": "P",
	"C": "S",
	"X": "R",
	"Y": "P",
	"Z": "S",
}

moveScores = {
	"R": 1,
	"P": 2,
	"S": 3,
}

resultMapping = {
	"RR": "D",
	"PP": "D",
	"SS": "D",
	"RP": "W",
	"PS": "W",
	"SR": "W",
	"RS": "L",
	"PR": "L",
	"SP": "L",
}

resultScores = {
	"L": 0,
	"D": 3,
	"W": 6,
}

score = 0
for theirMove, myMove in guide:
	game = moveMapping[theirMove] + moveMapping[myMove]
	score += moveScores[game[-1]]
	score += resultScores[resultMapping[game]]
print(score)



#  Part 2
score = 0
for theirMove, myMove in guide:
	game = moveMapping[theirMove] + moveMapping[myMove]
	score += moveScores[game[-1]]
	score += resultScores[resultMapping[game]]
print(score)

outcomeMapping = {
	"X": "L",
	"Y": "D",
	"Z": "W",
}

playMapping = {
	"RL": "S",
	"RD": "R",
	"RW": "P",
	"PL": "R",
	"PD": "P",
	"PW": "S",
	"SL": "P",
	"SD": "S",
	"SW": "R",
}

score = 0
for theirMove, outcome in guide:
	game = moveMapping[theirMove] + outcomeMapping[outcome]
	score += resultScores[game[-1]]
	score += moveScores[playMapping[game]]
print(score)