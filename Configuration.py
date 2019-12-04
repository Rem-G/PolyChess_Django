from Board import *
from Pieces import *
from Bot import *


class GeneralConf():
	def __init__(self):
		self.pieces = list()
		self.msg_error = list()
		self.board = Mat64()
		self.pieces_joueurB = list()
		self.pieces_joueurN = list()

	def add_piece(self, piece):
		"""
		@RG
		Ajoute une nouvelle pièce à la liste de pièces existantes
		"""
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
		return [{'nom': p.nom, 'position': p.position, 'joueur_blanc': p.nom.isupper()} for p in self.pieces]

	def pieces_joueurs(self):
		"""
		@NR
		Ajoute chaque piece a la liste des piece de chaque equipe
		"""

		for piece in self.pieces :
			if piece.nom.isupper():
				self.pieces_joueurB.append(piece)
			else:
				self.pieces_joueurN.append(piece)


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
			matrice[index_i] = i[1:len(
				i) - 1]  # Suppression du premier et dernier élément de la ligne -> suppression des -1
			for index_j, j in enumerate(i):
				try:  # Chaque ligne de la matrice étant redéfinie au dessus en supprimant la première et la dernière valeur
					# le maximum d'index_i est plus élevé que la taille de la nouvelle ligne
					if matrice[index_i][index_j] == -1:
						matrice[index_i][index_j] = '. '
				except:
					pass

		matrice_screen = matrice[2:len(matrice) - 2]

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
			# Vérification si la position d'arrivee correspond à un mouvement autorisé et qu'elle n'est pas à l'emplacement d'une pièce existante
			# Si la position d'arrivée correspond à l'emplacement d'une pièce existante, on vérifie si elle peut être mangée
			if self.board.matrice_jeu()[pos_arrivee[0]][pos_arrivee[1]] != -1:
				# Vérification si la position d'arrivée voulue est sur le plateau de jeu
				if pos_arrivee in possible_eat:
					# Supprime une pièce adverse si la position d'arrivée voulue correspond à l'emplacement d'une pièce adverse
					for piece in self.pieces:
						if pos_arrivee == piece.position:
							self.del_piece(piece)
				return True
		return False


	def sameTeam(self, piece1, piece2):
		""" @NR
		verifie si piece 1 et piece 2 sont dans le meme equipe
		:param piece1 : une piece
		:param piece2 : une piece
		:return bool : renvoie vrai si piece 1 et piece 2 sont dans la meme equipe
		"""
		if (piece1 in self.pieces_joueurB and piece2 in self.pieces_joueurB) or (piece1 in self.pieces_joueurN and piece2 in self.pieces_joueurN):
			return True
		return False


	def verification_deplacement_roi(self, roi, moves, pos_arrivee):
		""" @NR
		Verifie si le deplacement du roi est possible, sans l'emmener en echec
		:param roi: le roi
		:param moves: deplacements autorisés du roi
		:param pos_arrivee: Destination voulue par le joueur pour le roi
		:return bool : renvoie vrai si le deplacement est possible et faux sinon
		"""

		possible_moves = moves[0]
		possible_eat = moves[1]

		emplacements_pieces = list()
		[emplacements_pieces.append(piece.position) for piece in self.pieces]

		emplacements_reachable_by_opponent = list()
		for piece in self.pieces:
			if not (self.sameTeam(piece,roi)):  # si la piece courante n'est pas dans la meme equipe que le roi
				for erbo in piece.PossibleMoves()[1]:  # emplacement de capture de la piece enemie
					if erbo not in emplacements_reachable_by_opponent:  # Pour ne pas avoir de doublon
						emplacements_reachable_by_opponent.append(erbo)  # on ajoute les emplacements de capture de chaque piece

		if ((pos_arrivee in possible_moves and pos_arrivee not in emplacements_pieces) or (pos_arrivee in possible_eat)) and pos_arrivee not in emplacements_reachable_by_opponent:
			# verification si la position d'arrivee est dans les moves possibles et qu'il n'y pas de piece à cette emplacement ou que on peut manger une piece a cet emplacement
			# et que dans les deux cas la position d'arrivee ne soit pas un emplacement que pourrait prendre l'ennemi
			if self.board.matrice_jeu()[pos_arrivee[0]][pos_arrivee[1]] != -1:
				# Vérification si la position d'arrivée voulue est sur le plateau de jeu
				if pos_arrivee in possible_eat:
					# Supprime une pièce adverse si la position d'arrivée voulue correspond à l'emplacement d'une pièce adverse
					for piece in self.pieces:
						if pos_arrivee == piece.position:
							self.del_piece(piece)
				return True
		return False

	def tour_joueur(self, piece, pos_arrivee):
		"""
		@RG @NR
		Si le déplacement est autorisé, la position de la pièce change sinon affiche une erreur
		:param piece: Piece à vérifier
		:param pos_arrivee: Position d'arrivée désirée par le joueur pour la pièce
		"""

		if piece.__class__ is Roi :  # on regarde si la piece en question en roi, au quel cas on doit verifier si le move entraine un echec ou echec et matt
			roc_roi_fait = False
			if piece.firstMove == True : # roi n'a pas encore joue son premier tour
				#on essaie le roc
				roc_roi_fait = self.rocRoi(piece, pos_arrivee)

			if not (roc_roi_fait) and self.verification_deplacement_roi(piece, piece.PossibleMoves(), pos_arrivee):
				piece.set_piece_position(pos_arrivee)

			else:
				if not (roc_roi_fait):
					self.add_msg_error("déplacement interdit ou mise en échec du roi")

		else:

			if self.verification_deplacement(piece.PossibleMoves(), pos_arrivee):
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
		# Vérification que la valeur de la position de départ dans la matrice de jeu est différente de 1
		if self.board.valeur_position_piece_mat(pos_depart) != -1 and self.board.valeur_position_piece_mat(
				pos_arrivee) != -1:
			for piece in self.pieces:
				# Récupération et conversion des coordonnées utilisateur de la pièce en coordonnées de la matrice de jeu
				piece_x, piece_y = piece.get_piece_position()[0], piece.get_piece_position()[1]
				coordonnees_pieces.append([piece_x, piece_y])

				if piece_x == pos_depart[0] and piece_y == pos_depart[1]:
					# Vérification de la position actuelle de la pièce et de la position de départ demandée par l'utilisateur
					if upper is True:
						# Tour du joueur blanc
						if piece.nom.isupper():
							# Vérification nom piece, affiche un message d'erreur si ce déplacement est interdit
							self.tour_joueur(piece, pos_arrivee)

						else:
							self.add_msg_error("Cette pièce appartient à l'adversaire !")

					else:
						# Tour du joueur noir
						if piece.nom.islower():
							# Vérification nom piece, affiche un message d'erreur si ce déplacement est interdit
							self.tour_joueur(piece, pos_arrivee)

						else:
							self.add_msg_error("Cette pièce appartient à l'adversaire !")

			if pos_depart not in coordonnees_pieces:
				# Vérifie si la position de départ entrée par le joueur correspond à l'emplacement d'une pièce
				self.add_msg_error("Aucune pièce ne correspond à ces coordonnées")

		else:
			# Si le joueur entre des coordonnées en dehor du plateau de jeu
			self.add_msg_error("Merci de jouer sur le plateau")


	def rocRoi (self, roi, pos_arrivee):
		"""
		@NR
		applique le roc depuis le roi vers la tour
		:param roi : une piece roi
		:param pos_arrivee : la position d'arrivee, sur cette emplacement doit etre un roi ou une tour
		:return bool: true si le roc reussi, false sinon
		"""

		tour_allie = list()  # tour_allie : list des tours de tour allie
		for piece1 in self.pieces:
			if piece1.__class__ is Tour and self.sameTeam(roi, piece1):
				tour_allie.append(piece1)
		for tour in tour_allie:
			if tour.position == pos_arrivee:
				if tour.firstMove:
					print("roi y: ",roi.get_piece_position()[1], "tour y :",tour.get_piece_position()[1])
					for posCol in range (roi.get_piece_position()[1],tour.get_piece_position()[1]):  #on parcours l'echiquier sur l'horizontale entre les 2 pieces
						if posCol != roi.get_piece_position()[1] and self.case_occupe(roi.position[0],posCol): #on ne peut pas faire le roc, car il y a des piece entre la tour et le roi
							#pour ne pas qu'il commence a partir de la position du roi, on est oblige de faire comme ça car on ne connait pas le sens du parcours (ascendant ou descendannt)
							print("rocRoi")
							return False
					#on fait le roc avec une permutation
					line_roi = roi.get_piece_position()[0]
					col_roi = roi.get_piece_position()[1]
					line_tour = tour.get_piece_position()[0]
					col_tour=tour.get_piece_position()[1]

					if col_roi<col_tour:  #petit roc
						col_roi = col_roi +2
						col_tour = col_tour-2
					else:  #grant roc
						col_roi = col_roi-2
						col_tour = col_tour +3

					roi.set_piece_position([line_roi,col_roi])
					tour.set_piece_position([line_tour,col_tour])
					return True
		return False

	def case_occupe(self, posLine, posCol):
		"""
		@NR
		:param posLine: position ligne
		:param posCol: position colonne
		:return bool: True si la case est occupe, False sinon
		"""
		for piece in self.pieces:
			if piece.get_piece_position()==[posLine, posCol]:
				print(posLine, posCol)
				return True
		return False
