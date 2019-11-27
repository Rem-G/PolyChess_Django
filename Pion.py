class Pion:
    """
    Cette classe représentera la pièce pion et ses déplacements
    """

    def __init__(self, color, identifier, positionInitiale):
        self.color = color # Etabli la couleur du pion
        self.firstMove = True # Etabli l'etat du 1er move du pion
        self.id = identifier # Etabli l'identifiant du pion
        self.position = positionInitiale # Etabli la position initiale

    def firstMoveOver(self):
        """
        Permet de mettre à jour l'etat du 1er tour du pion
        """
        self.firstMove = False

    def newPosition(self, destination):
        """
        :param destination type (str, int): Coordonnees de la destination
        Met à jour la position du pion
        """
        self.position = destination

    def pawnPossibleMoves(self):
        """
        :return type list: Liste des moves possibles pour le pion
        """
        Destination = []
        if self.color == 'noir':
            Destination.append((self.position[0], self.position[1] + 1 * 8))
            if self.firstMove:
                Destination.append((self.position[0], self.position[1] + 2 * 8))
                self.firstMoveOver()
        else:
            Destination.append((self.position[0], self.position[1] - 1 * 8))
            if self.firstMove:
                Destination.append((self.position[0], self.position[1] - 2 * 8))
                self.firstMoveOver()
        return Destination

