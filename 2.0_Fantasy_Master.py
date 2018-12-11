#stats from: https://www.nbastuffer.com/2017-2018-nba-player-stats/

import csv
import matplotlib.pyplot as plt
import matplotlib


class Player:
	"""A player will have: name, position, 3pg, rpg, apg, spg, bpg, topg, and ppg"""
	def __init__(self, name, pos, tpg, rpg, apg, spg, bpg, topg, ppg):
		self.name = name
		self.pos = pos 
		self.tpg = tpg  
		self.rpg = rpg
		self.apg = apg
		self.spg = spg
		self.bpg = bpg
		self.topg = topg
		self.ppg = ppg

	#Setters
	def set_name(self, name):
		self.name = name
	def set_pos(self, pos):
		self.pos = pos
	def set_tpg(self, tpg):
		self.tpg = tpg
	def set_rpg(self, rpg):
		self.rpg = rpg
	def set_apg(self, apg):
		self.apg = apg
	def set_spg(self, spg):
		self.spg = spg
	def set_bpg(self, bpg):
		self.bpg = bpg
	def set_topg(self, topg):
		self.topg = topg
	def set_ppg(self, ppg):
		self.ppg = ppg




	#Getters
	def get_name(self):
		return self.name
	def get_pos(self):
		return self.pos
	def get_tpg(self):
		return self.tpg
	def get_rpg(self):
		return self.rpg
	def get_apg(self):
		return self.apg
	def get_spg(self):
		return self.spg
	def get_bpg(self):
		return self.bpg
	def get_topg(self):
		return self.topg
	def get_ppg(self):
		return self.ppg




p_list = [] #the list that will hold all qualified player list objects
qual_players = 0 #the number of players that qualify

with open('Week_8_Stats.csv') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=',')
	line_count = 0
	for row in csv_reader:
		if line_count == 0:
			line_count += 1
		
		elif row[0] == '':
			pass
		else:
			#helpful comments
			#print(f'Games Played by {row[1]} in 2017-2018 was {row[5]}')
			#print(f'Mins a game played by {row[1]} in 2017-2018 was {float(row[6])}')

			row[0] = Player(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
			p_list.append(row[0])
			qual_players += 1	
			line_count += 1
	print(f'Processed {line_count - 1} players.')
	print(f'There are {qual_players} qualified players.')


'''
Done getting the qualified players, now going to manipulate the data below...
'''


temp_three = 0
temp_rebs = 0
temp_ast = 0
temp_stl = 0
temp_blk = 0
temp_to = 0
temp_points = 0

for p in p_list:
	temp_three += float(p.get_tpg())
	temp_rebs += float(p.get_rpg())
	temp_ast += float(p.get_apg())
	temp_stl += float(p.get_spg())
	temp_blk += float(p.get_bpg())
	temp_to += float(p.get_topg())
	temp_points += float(p.get_ppg())

'''
League averages
'''
thre_avg_leag = temp_three / qual_players
reb_avg_leag = temp_rebs / qual_players
ast_avg_leag = temp_ast / qual_players
stl_avg_leag = temp_stl / qual_players
blk_avg_leag = temp_blk / qual_players
to_avg_leag = temp_to / qual_players
pts_avg_leag = temp_points / qual_players


print(f"the average 3's a game is {thre_avg_leag}")
print(f"the average points a game is {pts_avg_leag}")
print(f"the average rebounds a game is {reb_avg_leag}")
print(f"the average assists a game is {ast_avg_leag}")
print(f"the average steals a game is {stl_avg_leag}")
print(f"the average blocks a game is {blk_avg_leag}")
print(f"the average turnovers a game is {to_avg_leag}")





#this is the function that measures a players value in each category, and ultimately, their overall value.
#I might want to add these 7 new categories for each class(player) for their value in each category, or just 
#an overall value attribute.
def player_rater(name, p_three, p_rebs, p_ast, p_stl, p_blk, p_to, p_pts):
	if float(p_three) == 0.0:
		three_val = round(((0 - thre_avg_leag) / 0.0000000001), 3) #this can be changed to make 3's more, or less of a factor
		if three_val < -120.00: #since I am getting players with very low to zero numbers, I want to cap the influence it can have on a category.
			three_val =  -120.00
	else:
		three_val = round(((float(p_three) - thre_avg_leag) / thre_avg_leag) * 100, 3)
	if float(p_rebs) == 0:
		rebs_val = round(((0 - reb_avg_leag)/0.0000000001) * 100, 3)
		if rebs_val < -120.00:
			rebs_val = -120.00
	else:
		rebs_val =  round(((float(p_rebs) - reb_avg_leag) / reb_avg_leag) * 100, 3)
	if float(p_ast) == 0:
		ast_val = round(((0 - ast_avg_leag)/0.0000000001) * 100, 3)
		if ast_val < -120.00:
			ast_val = -120.00
	else:
		ast_val = round(((float(p_ast) - ast_avg_leag) / ast_avg_leag) * 100, 3)
	if float(p_stl) == 0:
		stl_val = round(((0 - stl_avg_leag)/0.0000000001) * 100, 3)
		if stl_val < -120.00:
			stl_val = -120.00
	else:
		stl_val = round(((float(p_stl) - stl_avg_leag) / stl_avg_leag) * 100, 3)
	if float(p_blk) == 0:
		blk_val = round(((0 - blk_avg_leag)/0.0000000001) * 100, 3)
		if blk_val < -120.00:
			blk_val = -120.00
	else:
		blk_val = round(((float(p_blk) - blk_avg_leag) / blk_avg_leag) * 100, 3)
	if float(p_to) == 0:
		to_val = round(((0 + to_avg_leag)/0.0000000001) * 100, 3)
		if to_val > 120.00:
			to_val = 120.00
	else:
		to_val = round(((float(p_to) - to_avg_leag) / to_avg_leag) * (-100), 3)
	if float(p_pts) == 0:
		pts_val = round(((0 - pts_avg_leag)/0.0000000001) * 100, 3)
		if pts_val < -120.00:
			pts_val = -120.00
	else:
		pts_val = round(((float(p_pts) - pts_avg_leag) / pts_avg_leag) * 100, 3)
	print(f"{name} scores. three val: {three_val}, rebs: {rebs_val}, ast: {ast_val}, stl: {stl_val}, blk: {blk_val}, to: {to_val}, pts: {pts_val}")
	ovr_val = round(three_val + rebs_val + ast_val + stl_val + blk_val + to_val + pts_val, 5)



	return ovr_val

#A function that sorts players by rating, then returns them in descending order
def sort_players(dict):
	p_rankings = sorted(dict.items(), key = lambda t:t[1]*-1)
	return p_rankings

max_value = 0
good_player_list = {}
for pl in p_list:
	x = player_rater(pl.get_name(), pl.get_tpg(), pl.get_rpg(), pl.get_apg(), pl.get_spg(), pl.get_bpg(), pl.get_topg(), pl.get_ppg())
	good_player_list[(pl.get_name())] = x

print()

#this will sort all players that qualify!
ranks = sort_players(good_player_list)
print("Player Ranks for the 2017-2018 Season:")
print()


#This class will hold less information than the Player class, but allows each player to have a rank and score.
#Might want to derivce from Player class in order to include stat categories (more info on given score)
class PRanked:
	def __init__(self, nam, score, rank, pos):
		self.nam = nam
		self.score = score
		self.rank = rank
		self.pos = pos

	def get_nam(self):
		return self.nam
	def get_score(self):
		return self.score
	def get_rank(self):
		return self.rank
	def get_pos(self):
		return self.pos


	def set_nam(self, nam):
		self.nam = nam
	def set_score(self, score):
		self.score = score
	def set_rank(self, rank):
		self.rank = rank
	def set_pos(self, pos):
		self.pos = pos

#now we can assign all of the ranked players to a class that has them in sorted order!

counter = 1
playerDict = {}

pg_list = {}
sg_list = {}
sf_list = {}
pf_list = {}
c_list = {}

pg_count = 0
sg_count = 0
sf_count = 0
pf_count = 0
c_count = 0

for player in ranks:
	pos_holder = ""
	for pla in p_list:
		if pla.get_name() == player[0]:
			pos_holder = pla.get_pos()

			if pla.get_pos() == 'PG' and pg_count < 15:
				pg_list[str(pg_count + 1) + ")" + pla.get_name()] =  player[1]
				pg_count +=1

			if pla.get_pos() == 'SG' and sg_count < 15:
				sg_list[str(sg_count + 1) + ")" + pla.get_name()] = player[1]
				sg_count +=1

			if pla.get_pos() == 'SF' and sf_count < 15:
				sf_list[str(sf_count + 1) + ")" + pla.get_name()] = player[1]
				sf_count +=1

			if pla.get_pos() == 'PF' and pf_count < 15:
				pf_list[str(pf_count + 1) + ")" + pla.get_name()] = player[1]
				pf_count +=1

			if pla.get_pos() == 'C' and c_count < 15:
				c_list[str(c_count + 1) + ")" + pla.get_name()] = player[1]
				c_count +=1


	x = player[0].replace(' ', "")
	x = PRanked(player[0], player[1], counter, pos_holder)
	print(f"{x.get_nam()} ({x.get_pos()}) is ranked {x.get_rank()} and has score {x.get_score()}")
	playerDict[player[0]] = x

	#scatter plot for each player!
	x_coor = x.get_pos()
	y_coor = x.get_score()
	plt.scatter(x_coor, y_coor)
	plt.xlabel('Position')
	plt.ylabel('Player Score')
	'''
	can annotate each point to have info like name for each individual.
	plt.annotate(f'{x.get_rank()}) {x.get_nam()} has score {x.get_score()}',
				 xy = (x_coor, y_coor), xytext = (x_coor + 1, y_coor))
	'''
	counter += 1



print()
respns = input("Type YES or NO to see top 15 lists for each position: ")
if respns == 'YES':
	print()
	print(f"Point Guards: {pg_list}")
	print()
	print(f"Shooting Guards: {sg_list}")
	print()
	print(f"Small Forwards: {sf_list}")	
	print()
	print(f"Power Forwards: {pf_list}")
	print()
	print(f"Centers: {c_list}")
else:
	print("not printing top 10 lists.")

total = 0
for pg in pg_list:
	total += pg_list[pg]
total = round(total, 3)
print(f"total PG scores: {total}")

total = 0
for sg in sg_list:
	total += sg_list[sg]
total = round(total, 3)
print(f"total SG scores: {total}")

total = 0
for sf in sf_list:
	total += sf_list[sf]
total = round(total, 3)
print(f"total SF scores: {total}")

total = 0
for pf in pf_list:
	total += pf_list[pf]
total = round(total, 3)
print(f"total PF scores: {total}")

total = 0
for c in c_list:
	total += c_list[c]
total = round(total, 3)
print(f"total C scores: {total}")

#showing the graph from 15 lines ago!
#plt.show()

#print(f"James Harden has a rank of: {playerDict['James Harden'].get_rank()}")	
'''
count = 1
rank_total = 0
while count < 14:
        name = input(f"Enter player {count}'s name on your team: ")
        if name in playerDict:
                print(f"{playerDict[name].get_nam()} has a rank of {playerDict[name].get_rank()}")
                count += 1
                rank_total += playerDict[name].get_rank()
        else:
                print("invalid player! Enter again.")
print(f"total ranks added up for your team: {rank_total}")
#print(f"the best player in this system is {max_player} with a score of {max_value}")
'''

'''
so I want to create a ranking system. The best way to start is to get the average, then compare each player to the average. 
I think I should only be using players that on average play a certain amount of minutes, otherwise the data will be lower than it should be.
Column 6 holds games played, I think I should exclude the player from statistics if they played less than 15 games (over 100 players removed this way)

Next I need to average out all of the stats! I think the best way to do it is to
divide total number of a category by the number of players in that category.

I am going to create an instance of the Player object for each player that qualifies.

My main problem now is getting to a player, because they should be created by name, but I do not know how to get to them... will come back to this later.

now, I am going to try and make the averages for the players in the league.

The next challenge is seeing which players are the best in this system. The trick is that certain players
do well in scoring but not as well in categories such as steals, which is inflated because the gap between points
will be bigger than the gap between steals, rebounds, and turnovers.

this is how to do it: measure % difference compared to league average.
equation: say we are measuring the % difference in points.

player points - league average = 'x'
x/player points = y
y * 100 = percentage change! Then just add up all of the percentage numbers to get a value!

Another problem I am having with this model is calculating the lost (or gained) value by having a zero for a category.
I don't really know how to measure the percentage value in that category. For now, I am leaving it as:
0 - league average
I will probably change this as I go, but for now it will work as a place holder I guess?

As I go throughout the season, I can simply format the data for the season into the same format as it is with 
my current csv file in excel, then run the program again to see which players are better/worse!

Next Challenge: certain players like steph curry have a 75.259 on threes, which is a good score,
but his value is very negatively affected by only getting 0.2 blocks a game, which knocks him down
183 points, far more than it should (I think).

If a player is at the best in their respective category, they usually receive a score in the mid
to high 80s for that category, but if they are bad, it can be usually as bad as -200.

To adjust this, I am going to try to cap negative values to -80 instead of -200
and see what the results are. 

Next step: include positional ranks (if wanted). Then I could determine quickly which players I want to
draft for a given position if I haven't yet drafter a Center, for example. 

I think I can do this within my for loop of line 309, what would be ideal is to just setup
7 counters, then ask the user if they want to see position rankings.

I think what I need to figure out next is why do players with good steals seem to always
push to the top. Almost all of my results have players with high steal numbers over all other cats.
I think this is just a product of the system, a lot of the players that are good with steals tend to be
good in other categories too, so I do not think this is a serious issue.

Next idea: Learning about plotting my data on some sort of graph. I want to give a players overall score
a boost or penalty based on trades, injuries or whatever the cause may be. 

The reason behind plotting this data is 1) because it looks cool and is way better than standard python output.
and 2) because if a player is only meant to temporarily have a boost or penalty, I want to be able to add 
a description about the boost/penalty, so that if the player say heals from injury, I can then remove the boost.
In adddition to this idea, it would be valuable to be able to see all current boosted/penaltied players
at once to keep tabs on which ones should no longer have a boost or penalty(basically to update all modified player values.).

The boost should affect the overall value at this point because I don't want to fidgit with which individual categories would be affected,
I think an overall value boost would be best in that sense. 


Now I am having an issue where players who hit 0 threes are getting a score that is better than those who hit 0.7 or so (like Anthony Davis and Andre Drummond):
Davis: 0.7 threes per game. Score: -73.712
Drummond: 0.0 Threes per game. Score: -59.799
'''













