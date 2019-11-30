from Board import *
from Pieces import *


class GeneralConf():
	def __init__(self):
		self.pieces = list()
		self.msg_error = list()
		self.board = Mat64()

	def add_piece(self, piece):
		"""
		@RG
		Ajoute une nouvelle pièce à la liste de pièces existantes
		"""
		piece.set_piece_id(len(self.pieces))
		self.pieces.append(piece)

	def test(self):
		for piece in self.pieces:
			print(piece.nom)


	def matrice_affichage(self):
		"""
		@RG
		Génère la matrice d'interface utilisateur en supprimant les lignes de -1 et affichant le nom de chaque pièce en fonction de leur emplacement
		sur l'échiquier 
		:return matrice_screen: Matrice 8*8 avec le nom des pièces affiché sur leur position, les -1 de la matrice initiale sont convertis en '.'
		"""
		pieces = self.pieces

		matrice = self.board.matrice_init()

		for piece in pieces:
			pos = self.board.position_piece_mat([piece.get_piece_position()[0], piece.get_piece_position()[1]])
			matrice[pos[0]][pos[1]] = piece.nom + ' '

		for index_i, i in enumerate(matrice):
			matrice[index_i] = i[1:len(i)-1] #Suppression du premier et dernier élément de la ligne -> suppression des -1
			for index_j, j in enumerate(i):
				try: #Chaque ligne de la matrice étant redéfinie au dessus en supprimant la première et la dernière valeur
					# le maximum d'index_i est plus élevé que la taille de la nouvelle ligne
					if matrice[index_i][index_j] == -1:
						matrice[index_i][index_j] = '. '
				except:
					pass

		matrice_screen = matrice[2:len(matrice)-2]

		return matrice_screen


	def deplacement_piece(self, pos_depart, pos_arrivee, upper):
		"""
		@RG
		Change de position une pièce selon la décision du joueur

		:param pos_depart: Position initiale de la pièce à bouger
		:param pos_depart: Position de destination de la pièce à bouger
		:param upper: Vérification du joueur faisant la requête : upper == True -> joueur blanc
		"""		
		pos_depart[1] = str(pos_depart[1]) #Conversion coordonée int en str
		pos_arrivee[1] = str(pos_arrivee[1])

		pos_depart_convert = self.board.position_piece_mat(pos_depart) #Conversion des coordonnées utilisateur de la pièce en coordonnées de la matrice de jeu
		pos_arrivee_convert = self.board.position_piece_mat(pos_arrivee)

		#Vérification que la valeur de la position de départ dans la matrice de jeu est différente de 1
		if self.board.valeur_position_piece_mat(pos_depart_convert) != -1 and self.board.valeur_position_piece_mat(pos_arrivee_convert) != -1:
			for piece in self.pieces:
				#Récupération et conversion des coordonnées utilisateur de la pièce en coordonnées de la matrice de jeu
				piece_x, piece_y = self.board.position_piece_mat(piece.get_piece_position())[0], self.board.position_piece_mat(piece.get_piece_position())[1]

				if piece_x == pos_depart_convert[0] and piece_y == pos_depart_convert[1]:
					#Vérification de la position actuelle de la pièce et de la position de départ demandée par l'utilisateur
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
		else:
			self.msg_error.append("Aucune pièce ne correspond à ces coordonnées")


