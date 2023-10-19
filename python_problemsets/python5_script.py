#!/usr/bin/env python3

import sys

fav_dict = {'book':'The Summoner Series','sport':'jiu-jitsu','os':'Windows','programming language':'python'}

fav_thing = 'organism'
fav_dict[fav_thing] = 'Xenpus Laevis'

#for thing in fav_dict:
#	print(thing, fav_dict[thing])

#for key in fav_dict:
#	print(key)

#print([key for key in fav_dict])

user_input = input(f'Which of these things do you want to know Robs favorite: {", ".join([key for key in fav_dict])}')

if user_input in fav_dict:
	print(fav_dict[user_input])
else:
	input(f"Rob doesn't care about {user_input}, try something else: ")

