from Board import Mat64

class Pion():
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

