class Bot():
	def __init__(self, pieces):
		self.pieces = pieces

	def position_pieces_blanc(self):
		"""
		@RG
		"""
		pos_pieces_b = list()
		for piece in self.pieces:
			if piece.nom.islower():
				pos_pieces_b.append(piece.position)
		return pos_pieces_b



