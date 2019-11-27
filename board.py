class Mat64():
	def __init__(self):
		pass

	def matrice_init(self):
		"""
		:return list: Renvoie la matrice initiale de taille 12*10
		"""
		return [[-1]*10 for i in range(12)]

	def game_aera(self):
		"""
		:return new_board: Echequier de taille 12*10 pour une surface de jeu de 8*8 permettant de gêrer les débordements
		"""
		board = self.matrice_init()
		new_board = list()
		[new_board.append([-1]*10) for k in range(2)]
		cpt = 0
		for i in board[2:len(board)-2]:
			k = i[:len(i)-1]
			for j in range(1,len(k)):
				k[j] = cpt
				cpt += 1
			k.append(-1)
			new_board.append(k)

		[new_board.append([-1]*10) for k in range(2)]
		return new_board

class Mat8():
	def __init__():
		pass

