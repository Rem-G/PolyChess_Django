from Board import Mat64

class Pion():
	def __init__(self, nom, pos_initiale):
		self.nom = nom
		self.position = pos_initiale
		self.position_convert = Mat64().position_piece_mat(pos_initiale)
		self.id = 0
		self.firstMove = True

	def set_piece_id(self, identifier):
		"""
		:param pieceId type int: Identifiant du pion
		Set l'identifiant du pion
		@TC
		"""
		self.id = identifier

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

	def firstMoveOver(self):
		"""
		Permet de mettre à jour l'etat du 1er tour du pion
		@TC
		"""
		self.firstMove = False

	def pawnPossibleMoves(self):
		"""
		:return type list: Liste des moves possibles pour le pion
		@TC
		"""
		moves, capture = [], []

		if self.nom == 'p':
			moves.append((self.position_convert[0] + 1, self.position_convert[1]))

			if self.firstMove:
				moves.append((self.position_convert[0] + 2, self.position_convert[1]))
				self.firstMoveOver()

			capture.append((self.position_convert[0] + 1, self.position_convert[1] - 1))
			capture.append((self.position_convert[0] + 1, self.position_convert[1] + 1))

		if self.nom == 'P':
			moves.append((self.position_convert[0] - 1, self.position_convert[1]))
			if self.firstMove:
				moves.append((self.position_convert[0] - 2, self.position_convert[1]))
				self.firstMoveOver()

			capture.append((self.position_convert[0] - 1, self.position_convert[1] - 1))
			capture.append((self.position_convert[0] - 1, self.position_convert[1] + 1))

		Destination = [moves, capture]

		return Destination


class Tour():
	def __init__(self, nom, pos_initiale):
		self.nom = nom
		self.position = pos_initiale
		self.id = 0

	def set_piece_id(self, pieceId):
		self.id = pieceId

	def get_piece_position(self):
		return self.position

	def set_piece_position(self, position):
		self.position = position


class Cavalier():
	def __init__(self, nom, pos_initiale):
		self.nom = nom
		self.position = pos_initiale
		self.position_convert = Mat64().position_piece_mat(pos_initiale)
		self.id = 0

	def set_piece_id(self, pieceId):
		self.id = pieceId

	def get_piece_position(self):
		return self.position

	def set_piece_position(self, position):
		self.position = position

class Fou():
	def __init__(self, nom, pos_initiale):
		self.nom = nom
		self.position = pos_initiale
		self.id = 0

	def set_piece_id(self, pieceId):
		self.id = pieceId

	def get_piece_position(self):
		return self.position

	def set_piece_position(self, position):
		self.position = position

class Dame():
	def __init__(self, nom, pos_initiale):
		self.nom = nom
		self.position = pos_initiale
		self.id = 0

	def set_piece_id(self, pieceId):
		self.id = pieceId

	def get_piece_position(self):
		return self.position

	def set_piece_position(self, position):
		self.position = position


class Roi():
	def __init__(self, nom, pos_initiale):
		self.nom = nom
		self.position = pos_initiale
		self.id = 0

	def set_piece_id(self, pieceId):
		self.id = pieceId

	def get_piece_position(self):
		return self.position

	def set_piece_position(self, position):
		self.position = position

