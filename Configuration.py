from Board import *
from Pieces import *


class GeneralConf():
	def __init__(self):
		self.pieces = list()
		self.msg_error = list()


	def add_piece(self, piece):
		piece.set_piece_id(len(self.pieces))
		self.pieces.append(piece)


	def matrice_affichage(self):
		"""
		"""
		pieces = self.pieces

		matrice = Mat64().matrice_init()

		for piece in pieces:
			pos = Mat64().position_piece([piece.get_piece_position()[0], piece.get_piece_position()[1]])
			matrice[pos[0]][pos[1]] = piece.nom + ' '

		for index_i, i in enumerate(matrice):
			matrice[index_i] = i[1:len(i)-1]
			for index_j, j in enumerate(i):
				try:
					if matrice[index_i][index_j] == -1:
						matrice[index_i][index_j] = '. '
				except:
					pass

		matrice_screen = matrice[2:len(matrice)-2]

		return matrice_screen


	def deplacement_piece(self, pos_depart, pos_arrivee, upper):
		"""
		"""		
		pos_depart[1] = str(pos_depart[1]) #Conversion coordonée int en str
		pos_arrivee[1] = str(pos_arrivee[1])


		pos_depart = Mat64().position_piece(pos_depart)

		for piece in self.pieces:
			piece_x, piece_y = Mat64().position_piece(piece.get_piece_position())[0], Mat64().position_piece(piece.get_piece_position())[1]

			try:
				if piece_x == pos_depart[0] and piece_y == pos_depart[1]:
					if upper is True:
						#Tour du joueur blanc
						if piece.nom.isupper():
							print('Pièce jouée :', piece.nom, piece.position, '->', pos_arrivee)
							piece.set_piece_position(pos_arrivee)

						else:
							self.msg_error.append("Cette pièce appartient à l'adversaire !")

					else:
						#Tour du joueur noir
						if piece.nom.islower():
							print('Pièce jouée :', piece.nom, piece.position, '->', pos_arrivee)
							piece.set_piece_position(pos_arrivee)

						else:
							self.msg_error.append("Cette pièce appartient à l'adversaire !")
			except:
				self.msg_error.append("Aucune pièce ne correspond à ces coordonnées")
				break


