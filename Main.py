'''
Projet PolyChess - PROJ531
VIEU Loïc
CENCI Thomas
RAZAFINDRABE Noah
GOSSELIN Rémi
'''

from Board import Mat64
from Pieces import Pion
from Configuration import *

def init_pieces(configuration):
	"""
	@RG
	Initialisation des pièces de jeu
	Les noms en masjuscule représentent les pièces blanches, et ceux en minuscule les pièces noires
	"""
	#Pieces blanches
	configuration.add_piece(Pion("P", ['a', '2']))
	configuration.add_piece(Pion("P", ['b', '2']))
	configuration.add_piece(Pion("P", ['c', '2']))
	configuration.add_piece(Pion("P", ['d', '2']))
	configuration.add_piece(Pion("P", ['e', '2']))
	configuration.add_piece(Pion("P", ['f', '2']))
	configuration.add_piece(Pion("P", ['g', '2']))
	configuration.add_piece(Pion("P", ['h', '2']))

	configuration.add_piece(Tour("T", ['a', '1']))
	configuration.add_piece(Tour("T", ['h', '1']))

	configuration.add_piece(Cavalier("C", ['b', '1']))
	configuration.add_piece(Cavalier("C", ['g', '1']))

	configuration.add_piece(Fou("F", ['c', '1']))
	configuration.add_piece(Fou("F", ['f', '1']))

	configuration.add_piece(Dame("D", ['d', '1']))

	configuration.add_piece(Roi("R", ['e', '1']))


	#Pieces noires
	configuration.add_piece(Pion("p", ['a', '7']))
	configuration.add_piece(Pion("p", ['b', '7']))
	configuration.add_piece(Pion("p", ['c', '7']))
	configuration.add_piece(Pion("p", ['d', '7']))
	configuration.add_piece(Pion("p", ['e', '7']))
	configuration.add_piece(Pion("p", ['f', '7']))
	configuration.add_piece(Pion("p", ['g', '7']))
	configuration.add_piece(Pion("p", ['h', '7']))

	configuration.add_piece(Tour("t", ['a', '8']))
	configuration.add_piece(Tour("t", ['h', '8']))

	configuration.add_piece(Cavalier("c", ['b', '8']))
	configuration.add_piece(Cavalier("c", ['g', '8']))

	configuration.add_piece(Fou("f", ['c', '8']))
	configuration.add_piece(Fou("f", ['f', '8']))

	configuration.add_piece(Dame("d", ['d', '8']))

	configuration.add_piece(Roi("r", ['e', '8']))

def affichage_plateau(matrice_affichage):
	"""
	@RG
	Mise en forme de la matrice d'affichage pour l'affichage utilisateur
	Ajout repère
	Composition des lignes du plateau
	"""
	ligne_valeurs = '   a b c d e f g h'
	colonne_valeurs = ['8', '7', '6', '5', '4', '3', '2', '1']
	ligne = 0

	for i in matrice_affichage:
		ch = str(colonne_valeurs[ligne] + '  ')
		ligne += 1
		for j in i:
			ch += str(j)
		print(ch)
	print('\n'+ligne_valeurs)


def decision_joueur(decision):
	"""
	@RG
	:param decision: Choix de jeu du joueur en str
	:return list: Choix de jeu du joueur en list
	"""
	pos_depart = decision.split(" ")[0].split(",")
	pos_arrivee = decision.split(" ")[1].split(",")

	return [pos_depart, pos_arrivee]

def game():
	"""
	@RG
	"""
	configuration = GeneralConf()

	init_pieces(configuration)

	affichage_plateau(configuration.matrice_affichage())

	joueur = 1

	while True:
		if joueur == 1:
			print("Au tour du joueur blanc :")
			decision = decision_joueur(input("Entrer x1,y1 x2,y2 :"))

			configuration.deplacement_piece(decision[0], decision[1], True)

		elif joueur == -1:
			print("Au tour du joueur noir :")
			decision = decision_joueur(input("Entrer x1,y1 x2,y2 :"))

			configuration.deplacement_piece(decision[0], decision[1], False)

		affichage_plateau(configuration.matrice_affichage())

		if len(configuration.msg_error):
			for msg in configuration.msg_error:
				print(msg)

		joueur = -joueur

game()
