import self as self # ?

###########################################################################################################
###### ATTENTION : il faudrait faire de l'heritage avec une classe piece comme classe mere cf.Trello ######
###########################################################################################################

class Pion:
    def __init__(self, nom, pos_initiale):
        self.nom = nom
        self.position = pos_initiale
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


class Roi:

    def __init__(self, nom, pos_initiale):
        """@NR
        :type nom: string
        """
        self.nom = nom
        self.position = pos_initiale
        self.id = 0

    def set_piece_id(self, pieceId):
        """ set l'indentifiant du roi @NR """
        self.id = pieceId

    def get_piece_position(self):
        """ return la position du roi @NR"""
        return self.position

    def set_piece_position(self, position):
        """
        position : (int,int) coordonnees de la destination
        set la position du roi @NR"""
        self.position = position

    def pawnPossibleMoves(self):
        """ return une liste des moves possibles pour le pion @NR"""
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


class Tour:
    def __init__(self, nom, pos_initiale):
        self.nom = nom
        self.position = pos_initiale
        self.id = 0

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


class Fou:
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


class Dame:
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
