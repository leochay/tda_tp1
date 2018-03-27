#!/usr/bin/python
import time
import random

def run_GaleShapely():

	#Parametros del problema
	teams_amount, players_amount = 20, 200;
	players_by_team = 10;

	#Se generan los sets de prueba aleatorios	
	players_preferences = [range(teams_amount) for y in range(players_amount)]
	for i in range(len(players_preferences)):
		random.shuffle(players_preferences[i]);
		for j in range(len(players_preferences[i])):
			print str(i)+", "+str(j) +":" + str(players_preferences[i][j]) + "\n";
	

	teams_preferences = [range(players_amount) for y in range(teams_amount)]
	for i in range(len(teams_preferences)):
		random.shuffle(teams_preferences[i]);
		for j in range(len(teams_preferences[i])):
			print str(i)+", "+str(j) +":" + str(teams_preferences[i][j]) + "\n";
	
	#Ejemplo: para acceder al 5to jugador preferido por el equipo 91: 
	#print teams_preferences[90][4]	
	#############################################################################

	#Implementacion del algoritmo
	teams_members = [[-1 for x in range(players_by_team)] for y in range(teams_amount)]
	#for i in range(len(teams_members)):
	#	for j in range(len(teams_members[i])):
	#		print str(i)+", "+str(j) +":" + str(teams_members[i][j]) + "\n";
	#	
	
	#Cada jugador se postula a su equipo preferido
	for i in range(players_amount):
		for j in range(teams_amount):
			#Si hay lugar en el team
			if -1 in teams_members[players_preferences[i][j]]:
				k = teams_members[players_preferences[i][j]].index(-1);
				teams_members[players_preferences[i][j]][k] = i;
				#TODO guardar el peor rankeado del team
				break;
			else:
			#TODO
			#Como no hay lugar, el team revisa si es que el candidato es mejor
			#que el peor rankeado de los actuales miembros
				print "No hay lugar en el team"

	print "="*20;
	print "Resultados:"
	for i in range(len(teams_members)):
		print "team " + str(i) + ": " + str(teams_members[i]);

def main():
	print "TP1 - Parte 2: Algoritmo de Gale Shapely"
	run_GaleShapely();
	
if __name__ == "__main__":
    main()
