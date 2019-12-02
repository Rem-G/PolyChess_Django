from Board import *
from Pieces import *
from Bot import *


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


	def del_piece(self, piece):
		"""
		@RG
		"""
		self.pieces.pop(self.pieces.index(piece))

	def add_msg_error(self, msg):
		"""
		@RG
		"""
		if msg not in self.msg_error:
			self.msg_error.append(msg)

	def infos_pieces(self):
		"""
		@RG
		Intérêt ?
		"""
		return [{'nom' : p.nom, 'id': p.id, 'position' : p.position} for p in self.pieces]


	def matrice_affichage(self):
		"""
		@RG
		Génère la matrice d'interface utilisateur en supprimant les lignes de -1 et affichant le nom de chaque pièce en fonction de leur emplacement
		sur l'échiquier 
		:return matrice_screen: Matrice 8*8 avec le nom des pièces affiché sur leur position, les -1 de la matrice initiale sont convertis en '.'
		"""
		matrice = self.board.matrice_init()

		for piece in self.pieces:
			pos = piece.get_piece_position()
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


	def verification_deplacement(self, moves, pos_arrivee):
		"""
		@RG
		Vérifie si pour les mouvements d'une pièce donnée, sa position d'arrivée est autorisée
		Prend en compte les déplacements classiques ainsi que les déplacements pour manger une pièce adverse
		:param moves: Déplacements autorisés de la pièce
		:param pos_arrivee: Destination voulue par le joueur pour la pièce
		:return bool: Renvoie vrai si le déplacement est autorisé, faux sinon
		"""
		possible_moves = moves[0]
		possible_eat = moves[1]

		emplacements_pieces = list()
		[emplacements_pieces.append(piece.position) for piece in self.pieces]

		if pos_arrivee in possible_moves and pos_arrivee not in emplacements_pieces or pos_arrivee in possible_eat:
			#Vérification si la position d'arrivee correspond à un mouvement autorisé et qu'elle n'est pas à l'emplacement d'une pièce existante
			#Si la position d'arrivée correspond à l'emplacement d'une pièce existante, on vérifie si elle peut être mangée
			if self.board.matrice_jeu()[pos_arrivee[0]][pos_arrivee[1]] != -1:
				#Vérification si la position d'arrivée voulue est sur le plateau de jeu
				if pos_arrivee in possible_eat:
					#Supprime une pièce adverse si la position d'arrivée voulue correspond à l'emplacement d'une pièce adverse
					for piece in self.pieces:
						if pos_arrivee == piece.position:
							self.del_piece(piece)
				return True
		return False


	def tour_joueur(self, piece, pos_arrivee):
		"""
		@RG
		Si le déplacement est autorisé, la position de la pièce change sinon affiche une erreur
		:param piece: Piece à vérifier
		:param pos_arrivee: Position d'arrivée désirée par le joueur pour la pièce
		"""
		if self.verification_deplacement(piece.pawnPossibleMoves(), pos_arrivee):
			piece.set_piece_position(pos_arrivee)

		else:
			self.add_msg_error("Déplacement interdit")


	def deplacement_piece(self, pos_depart, pos_arrivee, upper):
		"""
		@RG
		Change de position une pièce selon la décision du joueur

		:param pos_depart: Position initiale de la pièce à bouger
		:param pos_depart: Position de destination de la pièce à bouger
		:param upper: Vérification du joueur faisant la requête : upper == True -> joueur blanc
		"""	
		coordonnees_pieces = list()
		#Vérification que la valeur de la position de départ dans la matrice de jeu est différente de 1
		if self.board.valeur_position_piece_mat(pos_depart) != -1 and self.board.valeur_position_piece_mat(pos_arrivee) != -1:
			for piece in self.pieces:
				#Récupération et conversion des coordonnées utilisateur de la pièce en coordonnées de la matrice de jeu
				piece_x, piece_y = piece.get_piece_position()[0], piece.get_piece_position()[1]
				coordonnees_pieces.append([piece_x, piece_y])

				if piece_x == pos_depart[0] and piece_y == pos_depart[1]:
					#Vérification de la position actuelle de la pièce et de la position de départ demandée par l'utilisateur
					if upper is True:
						#Tour du joueur blanc
						if piece.nom.isupper():
							#Vérification nom piece, affiche un message d'erreur si ce déplacement est interdit
							self.tour_joueur(piece, pos_arrivee)

						else:
							self.add_msg_error("Cette pièce appartient à l'adversaire !")

					else:
						#Tour du joueur noir
						if piece.nom.islower():
							#Vérification nom piece, affiche un message d'erreur si ce déplacement est interdit
							self.tour_joueur(piece, pos_arrivee)

						else:
							self.add_msg_error("Cette pièce appartient à l'adversaire !")

			if pos_depart not in coordonnees_pieces:
				#Vérifie si la position de départ entrée par le joueur correspond à l'emplacement d'une pièce
				self.add_msg_error("Aucune pièce ne correspond à ces coordonnées")


