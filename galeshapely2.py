#!/usr/bin/python
import time
import random
import sys

FREE_POSITION = -1 #representa una posicion libre en un equipo

teams_amount, players_by_team, players_amount = 20, 10, 200
#teams_amount, players_by_team, players_amount = 3, 2, 6

def load_players_peferences():
	players_preferences = [range(teams_amount) for y in range(players_amount)]
	for i in range(len(players_preferences)):
		random.shuffle(players_preferences[i])
	return players_preferences

def load_teams_preferences():
	teams_preferences = [range(players_amount) for y in range(teams_amount)]
	for i in range(len(teams_preferences)):
		random.shuffle(teams_preferences[i])
	return teams_preferences

def pop_top_ranked_peference(preferences):
	return preferences.pop(0)
"""
#Esto es O(players_amount)	
	for preference_index in range(len(preferences)):
		if(preferences[preference_index] != FREE_POSITION):
			result = preferences[preference_index]
			preferences[preference_index] = FREE_POSITION
			return result
	raise Exception('No hay mas preferencias no utilizadas disponibles.') 
"""
def init_teams():
	teams = [[FREE_POSITION for x in range(players_by_team)] for y in range(teams_amount)]
	return teams

#O(players_by_team)
def team_vacancies_available(team):
	return FREE_POSITION in team

#Devuelve true si hay al menos un team con vacantes.
"""
En el peor de los casos, el team con vacantes es el ultimo, 
y la ultima vacante en ese team esta en la ultima posicion
asi que es O(teams_amount*players_by_team)
"""
def vacancies_available(teams):
	for team_number in range(teams_amount):
		if(team_vacancies_available(teams[team_number])):
			return True
	return False

def add_player_to_team(team, player_number):
	team[team.index(FREE_POSITION)] = player_number

def remove_player_from_team(team, player_number):
	team[team.index(player_number)] = FREE_POSITION

def move_player(from_team, to_team, player_number):
	remove_player_from_team(from_team, player_number)
	add_player_to_team(to_team, player_number)

def compare_preferences(preferences, a_number, b_number):
	a_rank = preferences.index(a_number)
	b_rank = preferences.index(b_number)
	if(a_rank < b_rank):
		return 1
	elif (a_rank > b_rank):
		return -1
	else:
		return 0

#En el peor caso, al jugador se lo encuentra
#en el ultimo team, en la ultima posicion
#O(teams_amount*players_by_team)
def find_player(teams, player_number):
	for team_number in range(teams_amount):
		if player_number in teams[team_number]:
			return team_number
	return FREE_POSITION

#O(teams_amount**2 players_by_team**3)  
# Entonces:
# GS modificado es (20*20)*(1000) = 400*1000 = 400000
# GS comun es O(teams_amount*players_amount) => 20*200 = 4000   
def run_gale_shapely(teams, teams_preferences, players_preferences):
	while vacancies_available(teams): #O(teams_amount*players_by_team)
		for team_number in range(teams_amount):
			while team_vacancies_available(teams[team_number]): #O(players_by_team)
				#team_preference = pop_top_ranked_peference(teams_preferences[team_number])#modificado para que sea O(1)
				team_preference = teams_preferences[team_number].pop(0)
				#Si el jugador esta libre
				other_team_number = find_player(teams, team_preference) #O(teams_amount*players_by_team)
				if(other_team_number == FREE_POSITION):
					add_player_to_team(teams[team_number], team_preference)
				else:
					if(compare_preferences(players_preferences[team_preference], team_number, other_team_number) > 0):
						move_player(teams[other_team_number], teams[team_number], team_preference)
				print("\n")
				print_everything(teams_preferences, players_preferences, teams)
			print("\n")
			print_everything(teams_preferences, players_preferences, teams)
		print("\n")
		print_everything(teams_preferences, players_preferences, teams)

def print_preferences(preferences):
	preferences_str = [str(x) for x in preferences]
	for i in range(len(preferences_str)):
		sys.stdout.write(str(i) + ":")
		print preferences[i]
		sys.stdout.flush()

def print_everything(teams_preferences, players_preferences, teams) :
	print "Preferencias de los equipos:"
	print_preferences(teams_preferences)

	print "Preferencias de los jugadores:"
	print_preferences(players_preferences)

	print "Equipos formados:"
	print_preferences(teams)

	sys.stdout.flush()
	time.sleep(0.1)

def main():
	print "TP1 - Parte 2: Algoritmo de Gale Shapely"

	teams_preferences = load_teams_preferences()
	players_preferences = load_players_peferences()
	teams = init_teams()

	print_everything(teams_preferences, players_preferences, teams)

	run_gale_shapely(teams, teams_preferences, players_preferences)
	
if __name__ == "__main__":
    main()
