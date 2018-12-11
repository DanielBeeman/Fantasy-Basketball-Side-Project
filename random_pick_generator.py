#Random pick generator program
import time
import random

'''
Teams:

Matthew Hval 
Tristan Le
Kirk Bassett
Brandon Le
Chandler Potter
Nina Hernandez
Laurent Mais
Dan HL
Mark Arellano
Daniel Beeman

'''

teams = ["Mathew Hval", "Trisan Le", "Kirk Bassett", "Brandon Le", "Chandler Potter",
 "Nina Hernandez", "Laurent Mais", "Dan HL", "Mark Arellano", "Daniel Beeman"]


counter = 1
while counter < 11:
	time.sleep(3)
	x = random.choice(teams)
	print(f"{x} has pick {counter}!")
	teams.remove(x)
	counter += 1

