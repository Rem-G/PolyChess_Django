class Mat64():
	def __init__(self):
		pass

	def matrice_init(self):
		"""
		-1 représente une zone non accessible par une pièce de jeu
		:return list: Renvoie la matrice initiale de taille 12*10
		"""
		return [[-1]*10 for i in range(12)]

	def game_aera(self):
		"""
		-1 représente une zone non accessible par une pièce de jeu
		:return new_board: Echequier de taille 12*10 pour une surface de jeu de 8*8 permettant de gêrer les débordements
		"""
		board = self.matrice_init()
		new_board = list()
		[new_board.append([-1]*10) for k in range(2)]
		pos = 0
		for i in board[2:len(board)-2]:
			k = i[:len(i)-1]
			for j in range(1,len(k)):
				k[j] = pos
				pos += 1
			k.append(-1)
			new_board.append(k)

		[new_board.append([-1]*10) for k in range(2)]
		return new_board


	def position_init_pieces(self, piece):
		"""
		:param piece: position initiale de la piece
		:return nom_piece: Renvoie le nom de la pièce en fonction de sa position initiale passée en paramètre
		"""
		pieces = {'P': [48,49,50,51,52,53,54,55], 'p': [8, 9, 10, 11, 12, 13, 14, 15], 'T' : [56, 63], 't' : [0, 7], 'C' : [57, 62], 'c' : [1, 6], 'F' : [58, 61], 'f' :[2, 5], 'D' : [59], 'd' : [3], 'R' : [60], 'r' : [4] }
		
		for nom_piece, pos_piece in pieces.items():
			if piece in pos_piece:
				return nom_piece

	def position_piece(self, piece):
		"""
		:return list: Renvoie la position de la pièce dans le référentiel de la matrice de l'échéquier
		"""
		lignes_matrice = {'h' : 2, 'g' : 3, 'f' : 4, 'e' : 5, 'd': 6, 'c' : 7, 'b' : 8, 'a' : 9}
		colonnes_matrice = {'8' : 1, '7' : 2, '6' : 3, '5' : 4, '4' : 5, '3' : 6, '2' : 7, '1' : 8 }

		board = self.game_aera()

		return [colonnes_matrice[piece[1]], lignes_matrice[piece[0]]]

