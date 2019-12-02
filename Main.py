'''
Projet PolyChess - PROJ531
VIEU Loïc
CENCI Thomas
RAZAFINDRABE Noah
GOSSELIN Rémi
'''
from Configuration import *

def init_pieces(configuration):
	"""
	@RG
	Initialisation des pièces de jeu
	Les noms en masjuscule représentent les pièces blanches, et ceux en minuscule les pièces noires
	"""
	#Pieces blanches
	configuration.add_piece(Pion("P", [8, 1]))
	configuration.add_piece(Pion("P", [8, 2]))
	configuration.add_piece(Pion("P", [8, 3]))
	configuration.add_piece(Pion("P", [8, 4]))
	configuration.add_piece(Pion("P", [8, 5]))
	configuration.add_piece(Pion("P", [8, 6]))
	configuration.add_piece(Pion("P", [8, 7]))
	configuration.add_piece(Pion("P", [8, 8]))

	configuration.add_piece(Tour("T", [9, 1]))
	configuration.add_piece(Tour("T", [9, 8]))

	configuration.add_piece(Cavalier("C", [9, 2]))
	configuration.add_piece(Cavalier("C", [9, 7]))

	configuration.add_piece(Fou("F", [9, 3]))
	configuration.add_piece(Fou("F", [9, 6]))

	configuration.add_piece(Dame("D", [9, 4]))

	configuration.add_piece(Roi("R", [9, 5]))


	#Pieces noires
	configuration.add_piece(Pion("p", [3, 1]))
	configuration.add_piece(Pion("p", [3, 2]))
	configuration.add_piece(Pion("p", [3, 3]))
	configuration.add_piece(Pion("p", [3, 4]))
	configuration.add_piece(Pion("p", [3, 5]))
	configuration.add_piece(Pion("p", [3, 6]))
	configuration.add_piece(Pion("p", [3, 7]))
	configuration.add_piece(Pion("p", [3, 8]))

	configuration.add_piece(Tour("t", [2, 1]))
	configuration.add_piece(Tour("t", [2, 8]))

	configuration.add_piece(Cavalier("c", [2, 2]))
	configuration.add_piece(Cavalier("c", [2, 7]))

	configuration.add_piece(Fou("f", [2, 3]))
	configuration.add_piece(Fou("f", [2, 6]))

	configuration.add_piece(Dame("d", [2, 4]))

	configuration.add_piece(Roi("r", [2, 5]))

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


def decision_joueur(decision, configuration):
	"""
	@RG
	:param decision: Choix de jeu du joueur en str
	:return list: Choix de jeu du joueur en list
	"""

	pos_depart = configuration.board.position_piece_mat(decision.split(" ")[0].split(","))
	pos_arrivee = configuration.board.position_piece_mat(decision.split(" ")[1].split(","))

	pos_depart = [int(pos) for pos in pos_depart]
	pos_arrivee = [int(pos) for pos in pos_arrivee]

	return [pos_depart, pos_arrivee]

def game_pvp():
	"""
	@RG
	"""
	configuration = GeneralConf()

	init_pieces(configuration)

	affichage_plateau(configuration.matrice_affichage())

	joueur = 1
	print(configuration.pieces[15].nom)
	print(configuration.pieces[15].get_piece_position())
	print(configuration.pieces[15].pawnPossibleMoves())

	while True:
		if joueur == 1:
			print("\nAu tour du joueur blanc :")
			input_value = input("Entrer x1,y1 x2,y2 :")
			print("\n")

			decision = decision_joueur(input_value, configuration)
			configuration.deplacement_piece(decision[0], decision[1], True)


		elif joueur == -1:
			print("\nAu tour du joueur noir :")
			input_value = input("Entrer x1,y1 x2,y2 :")
			print("\n")

			decision = decision_joueur(input_value, configuration)
			configuration.deplacement_piece(decision[0], decision[1], False)

		affichage_plateau(configuration.matrice_affichage())

		if len(configuration.msg_error):
			for msg in configuration.msg_error:
				print(msg)

		if not len(configuration.msg_error):
			joueur = -joueur

		configuration.msg_error = list()

game_pvp()
