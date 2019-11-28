'''
Projet PolyChess - PROJ531
VIEU Loïc
CENCI Thomas
RAZAFINDRABE Noah
GOSSELIN Rémi
'''

from board import Mat64
plateau = Mat64().game_aera()

def affichage_plateau():
	"""
	"""
	ligne_valeurs = '   8 7 6 5 4 3 2 1'
	colonne_valeurs = ['h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']

	print(ligne_valeurs)

	cpt = 0
	ligne = 0
	for k in plateau :
		for y in k:
			if y == -1:
				cpt += 1
		if cpt <= 2:
			ch = str(colonne_valeurs[ligne] + '  ')
			ligne += 1
			for i in k:
				if Mat64().position_init_pieces(i) != None and i != -1:
					ch += Mat64().position_init_pieces(i) + ' '
				elif i != -1:
					ch += '. '
			print(ch)
		cpt = 0

affichage_plateau()

print(Mat64().position_piece(('a','2')))
