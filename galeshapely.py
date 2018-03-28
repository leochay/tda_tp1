#!/usr/bin/python
import time
import random

FREE_POSITION = -1 #representa una posicion libre en un equipo

def run_gale_shapely():

	#Parametros del problema
	teams_amount, players_amount = 20, 200;
	players_by_team = 10;
	
	#teams_amount, players_amount = 2, 10;
	#players_by_team = 5;

	#Se generan los sets de prueba aleatorios	
	print "players preferences"
	players_preferences = [range(teams_amount) for y in range(players_amount)]
	for i in range(len(players_preferences)):
		random.shuffle(players_preferences[i]);
		for j in range(len(players_preferences[i])):
			print str(i)+","+str(j) +": " + str(players_preferences[i][j]) + "\n";
	

	print "teams preferences"
	teams_preferences = [range(players_amount) for y in range(teams_amount)]
	for i in range(len(teams_preferences)):
		random.shuffle(teams_preferences[i]);
		for j in range(len(teams_preferences[i])):
			print str(i)+","+str(j) +": " + str(teams_preferences[i][j]) + "\n";
	
	#Ejemplo: para acceder al 5to jugador preferido por el equipo 19: 
	#print teams_preferences[18][4]	
	#############################################################################

	#Implementacion del algoritmo
	
	#Matriz que contiene los miembros finales de cada equipo y al final el miembro peor rankeado.
	# (team_members[x][players_by_team] contendra siempre el peor rankeado del equipo x)
	teams_members = [[FREE_POSITION for x in range(players_by_team + 1)] for y in range(teams_amount)]
	
	#Conjunto de jugadores que aun no consiguen equipo.
	free_players = set(range(players_amount))
	
	#Cada jugador se postula a su equipo preferido
	while free_players:
		i = free_players.pop()
		for j in range(teams_amount):
			#El team al que se postula
			team = teams_members[ players_preferences[i][j]]
			
			#Si hay algun lugar libre en el team
			if FREE_POSITION in team[:len(team)-1]:
				k = team[:len(team)-1].index(FREE_POSITION) # devuelve el primero libre
				team[k] = i; # se agrega el jugador al team
					
				#Se guarda el peor rankeado del team
				#En que posicion esta el jugador que quiero agregar
				player_ranking_position = teams_preferences[j].index(i)

				if player_ranking_position > team[players_by_team]:
					team[players_by_team] = player_ranking_position
				
				#free_players.remove(i)
				break;

			else:
				#Como no hay lugar, el team revisa si es que el candidato es mejor
				#que el peor rankeado de los actuales miembros
				print "No hay lugar en el team, revisando si el candidato es mejor que alguno ya incluido..."
				
				player_ranking_position = teams_preferences[j].index(i)

				if player_ranking_position < team[players_by_team]:
					#se reemplaza al jugador
					print "El nuevo candidato es mejor"
					id_worst_player = teams_preferences[j][team[players_by_team]]
					print "id_worst_player: " + str(id_worst_player)
					team[ team.index(id_worst_player)] = i #se agrega el jugador al team
						
					id_new_worst_player = i
					#se actualiza el raking del peor rankeado
					for current_member_id in team[:len(team)-1]:
						if current_member_id != FREE_POSITION:
							if teams_preferences[j].index(current_member_id) > id_new_worst_player:
								id_new_worst_player = current_member_id
							
					team[players_by_team] = teams_preferences[j].index(id_new_worst_player)
						
					#free_players.remove(i)
					free_players.add(id_worst_player) #se devuelve al jugador al set de libres
					break;
		

	print "="*20;
	print "Resultados:"
	for i in range(len(teams_members)):
		print "team " + str(i) + ": " + str(teams_members[i]);

def main():
	print "TP1 - Parte 2: Algoritmo de Gale Shapely"
	run_gale_shapely()
	
if __name__ == "__main__":
    main()
