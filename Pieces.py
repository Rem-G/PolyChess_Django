class Pion():
	def __init__(self, nom, pos_initiale):
		self.nom = nom
		self.position = pos_initiale
		self.id = 0
		self.firstMove = True

	def set_piece_id(self, identifier):
		"""
		:param pieceId type int: Identifiant du pion
		Set l'identifiant du pion
		"""
		self.id = identifier

	def get_piece_position(self):
		return self.position

	def set_piece_position(self, position):
		"""
		:param position type (str, int): Coordonnees de la destination
		Met à jour la position du pion
		"""
		self.position = position

	def firstMoveOver(self):
		"""
		Permet de mettre à jour l'etat du 1er tour du pion
		"""
		self.firstMove = False

	def pawnPossibleMoves(self):
		"""
		:return type list: Liste des moves possibles pour le pion
		"""
		Destination = []

		if self.nom == 'p':
			Destination.append((self.position[0], self.position[1] + 1))
			if self.firstMove:
				Destination.append((self.position[0], self.position[1] + 2))
				self.firstMoveOver()

		if self.nom == 'P':
			Destination.append((self.position[0], self.position[1] - 1))
			if self.firstMove:
				Destination.append((self.position[0], self.position[1] - 2))
				self.firstMoveOver()

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

