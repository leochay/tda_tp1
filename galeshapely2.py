#!/usr/bin/python
import time
import random
import sys

FREE_POSITION = -1 #representa una posicion libre en un equipo

#Dimensiones del problema:
teams_amount, players_by_team, players_amount = 20, 10, 200
#teams_amount, players_by_team, players_amount = 3, 2, 6

def load_players_peferences():
	players_preferences = [range(teams_amount) for y in range(players_amount)]
	for i in range(players_amount):
		file_name = './setDePruebasParte2/'+'jugador_['+str(i+1)+'].prf'
		with open(file_name, 'r') as preference_list:
			pl = [int(j) for j in list(preference_list)]
			players_preferences[i] = pl
	return players_preferences
	
def load_teams_preferences():
	teams_preferences = [range(players_amount) for y in range(teams_amount)]
	for i in range(teams_amount):
		file_name = './setDePruebasParte2/'+'equipo_['+str(i+1)+'].prf'
		with open(file_name, 'r') as preference_list:
			pl = [int(j) for j in list(preference_list)]
			teams_preferences[i] = pl
	return teams_preferences

#Genera un set de archivos de prueba en el directorio setDePruebasParte2
#Para equipos: equipo_[nro].prf => generate_test_set(teams_amount, players_amount, 'equipo')
#Para jugadores: jugador_[nro].prf => generate_test_set(players_amount, teams_amount, 'jugador')
def generate_test_set(files_amount, lines_amount, file_name_prefix):
	for i in range(files_amount):
		file_name = './setDePruebasParte2/'+file_name_prefix+'_['+str(i+1)+'].prf'	
		fh = open(file_name,'w')
		members_ranking = range(lines_amount)
		random.shuffle(members_ranking)
		for j in members_ranking:
		  fh.write("%s\n" % (j+1))
		fh.close()
		
def init_teams():
	teams = [[FREE_POSITION for x in range(players_by_team)] for y in range(teams_amount)]
	return teams

def team_vacancies_available(team):
	return FREE_POSITION in team

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

def find_player(teams, player_number):
	for team_number in range(teams_amount):
		if player_number in teams[team_number]:
			return team_number
	return FREE_POSITION

def run_gale_shapely(teams, teams_preferences, players_preferences):
	vacancies_available = teams_amount * players_by_team
	team_vacancies_available = [players_by_team for x in range(teams_amount)]
	while vacancies_available > 0:
		for team_number in range(teams_amount):
			while team_vacancies_available[team_number]:
				team_preference = teams_preferences[team_number].pop(0)
				other_team_number = find_player(teams, team_preference)
				if(other_team_number == FREE_POSITION):
					add_player_to_team(teams[team_number], team_preference)
					vacancies_available -= 1
					team_vacancies_available[team_number] -= 1
				else:
					if(compare_preferences(players_preferences[team_preference-1], team_number+1, other_team_number+1) > 0):
						move_player(teams[other_team_number], teams[team_number], team_preference)
						team_vacancies_available[other_team_number] += 1
						team_vacancies_available[team_number] -= 1

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

#	generate_test_set(teams_amount, players_amount, 'equipo')
#	generate_test_set(players_amount, teams_amount, 'jugador')

	teams_preferences = load_teams_preferences()
	players_preferences = load_players_peferences()
	teams = init_teams()

	run_gale_shapely(teams, teams_preferences, players_preferences)
	
	print_everything(teams_preferences, players_preferences, teams)
	
	return teams

	
#Genera la tabla de jugadores y equipos en LaTeX para el informe
def to_latex(matrix):
	column_definition = "|".join(["c" for x in range(len(matrix[0]))])
	print("\\begin{center}")
	print("\\begin{longtable}{ |" + column_definition + "| } ")
	print(" \\hline")
	
	for row in range(len(matrix)):
		sys.stdout.write(" & ".join(map(str, matrix[row])) + " \\\\\n")

	print(" \\hline")
	print("\\end{longtable}")
	print("\\end{center}")

def players_preferences_to_latex():
	preferences = load_players_peferences()
	matrix = [range(len(preferences))] + zip(*preferences)
	matrix = zip(*matrix)
	to_latex(matrix)
	
def teams_preferences_to_latex():
	preferences = load_teams_preferences()
	matrix = [range(len(preferences))] + zip(*preferences)
	to_latex(matrix)

def results_to_latex():
	results = main()
	matrix = [range(len(results))] + zip(*results)
	to_latex(matrix)
	
if __name__ == "__main__":
	main()