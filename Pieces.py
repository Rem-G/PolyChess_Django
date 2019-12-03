class Piece():#Classe mère
	def __init__(self, nom, pos_initiale):
		self.nom = nom
		self.position = pos_initiale

	def get_piece_position(self):
		"""
		@TC
		"""
		return self.position

	def set_piece_position(self, position):
		"""
		:param position type (int, int): Coordonnees de la destination
		Met à jour la position du pion
		@TC
		"""
		self.position = position

###########################################################################################################
###########################################################################################################

class Pion(Piece):
	def __init__(self, nom, pos_initiale):
		super().__init__(nom, pos_initiale)
		self.firstMove = True

	def firstMoveOver(self):
		"""
		Permet de mettre à jour l'etat du 1er tour du pion
		@TC
		"""
		self.firstMove = False

	def PossibleMoves(self):
		"""
		:return type list: Liste des moves possibles pour le pion
		@TC
		"""
		moves, capture = [], []

		if self.nom == 'p':
			moves.append([self.position[0] + 1, self.position[1]])

			if self.firstMove:
				moves.append([self.position[0] + 2, self.position[1]])
				self.firstMoveOver()

			capture.append([self.position[0] + 1, self.position[1] - 1])
			capture.append([self.position[0] + 1, self.position[1] + 1])

		if self.nom == 'P':
			moves.append([self.position[0] - 1, self.position[1]])
			if self.firstMove:
				moves.append([self.position[0] - 2, self.position[1]])
				self.firstMoveOver()

			capture.append([self.position[0] - 1, self.position[1] - 1])
			capture.append([self.position[0] - 1, self.position[1] + 1])

		destination = [moves, capture]

		return destination

###########################################################################################################
###########################################################################################################


class Roi(Piece):

	def __init__(self, nom, pos_initiale):
		"""@NR
		:type nom: string
		"""
		super().__init__(nom, pos_initiale)
		self.firstMove = True
		self.check = False
		self.checkMate = False


	def firstMoveOver(self):
		"""
		Permet de mettre à jour l'etat du 1er tour du pion
		@TC
		"""
		self.firstMove = False


	def PossibleMoves(self):
		""" return une liste des moves possibles pour le roi @NR"""
		# je teste avec les coordonnees carstesiennes pas avec les coordonnes de l'echiquer

		x = self.position[0]
		y = self.position[1]

		# pour moi move et capture sont les meme

		moves = []  # list de move qui sont aussi des listes
		for i in range(-1, 2):
			for j in range(-1, 2):
				if i != 0 or j != 0:
					moves.append([x + i,y + j])  # on ajoute dans la liste toutes les cases autour de lui sans sa position courante
		return [moves,moves]

###########################################################################################################
###########################################################################################################

class Tour(Piece):
	def __init__(self, nom, pos_initiale):
		super().__init__(nom, pos_initiale)
		self.firstMove = True

	def firstMoveOver(self):
		"""
		Permet de mettre à jour l'etat du 1er tour du pion
		@TC
		"""
		self.firstMove = False

###########################################################################################################
###########################################################################################################

class Cavalier(Piece):
	def __init__(self, nom, pos_initiale):
		super().__init__(nom, pos_initiale)

###########################################################################################################
###########################################################################################################


class Fou(Piece):
	def __init__(self, nom, pos_initiale):
		super().__init__(nom, pos_initiale)

###########################################################################################################
###########################################################################################################


class Dame(Piece):
	def __init__(self, nom, pos_initiale):
		super().__init__(nom, pos_initiale)

