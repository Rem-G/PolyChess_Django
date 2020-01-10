'''
Projet PolyChess - PROJ531
VIEU Loïc
CENCI Thomas
RAZAFINDRABE Noah
GOSSELIN Rémi
'''
from .Configuration import *


# test commit

class Main:
    def __init__(self):
        self.joueur = 1

    def init_pieces(self, configuration):
        """
        @RG @RN
        Initialisation des pièces de jeu
        Les noms en masjuscule représentent les pièces blanches, et ceux en minuscule les pièces noires
        Coordonnées en 12*10
        """
         # Pieces blanches
        configuration.add_piece(Pion("P", [8, 1]))
        configuration.add_piece(Pion("P", [8, 2]))
        configuration.add_piece(Pion("P", [8, 3]))
        configuration.add_piece(Pion("P", [8, 4]))
        configuration.add_piece(Pion("P", [8, 5]))
        configuration.add_piece(Pion("P", [8, 6]))
        configuration.add_piece(Pion("P", [8, 7]))
        configuration.add_piece(Pion("P", [8, 8]))
        
        configuration.add_piece(Tour("T", [9, 1]))
        configuration.add_piece(Tour("T", [9, 8]))
        
        configuration.add_piece(Cavalier("C", [9, 2]))
        configuration.add_piece(Cavalier("C", [9, 7]))
        
        configuration.add_piece(Fou("F", [9, 3]))
        configuration.add_piece(Fou("F", [9, 6]))
        
        configuration.add_piece(Dame("D", [9, 4]))
        
        roiB = Roi("R", [9, 5])
        configuration.add_piece(roiB)
        configuration.init_roi(roiB)
        
        # Pieces noires
        configuration.add_piece(Pion("p", [3, 1]))
        configuration.add_piece(Pion("p", [3, 2]))
        configuration.add_piece(Pion("p", [3, 3]))
        configuration.add_piece(Pion("p", [3, 4]))
        configuration.add_piece(Pion("p", [3, 5]))
        configuration.add_piece(Pion("p", [3, 6]))
        configuration.add_piece(Pion("p", [3, 7]))
        configuration.add_piece(Pion("p", [3, 8]))
        
        configuration.add_piece(Tour("t", [2, 1]))
        configuration.add_piece(Tour("t", [2, 8]))
        
        configuration.add_piece(Cavalier("c", [2, 2]))
        configuration.add_piece(Cavalier("c", [2, 7]))
        
        configuration.add_piece(Fou("f", [2, 3]))
        configuration.add_piece(Fou("f", [2, 6]))
        
        configuration.add_piece(Dame("d", [2, 4]))
        
        roiN = Roi("r", [2, 5])
        configuration.add_piece(roiN)
        configuration.init_roi(roiN)


    def decision_joueur(self, decision, configuration):
        """
        @RG
        :param decision: Choix de jeu du joueur en str
        :return list: Choix de jeu du joueur en list
        """

        # Conversion des coordonnées utilisateur en coordonnées matricielles

        decision = decision.split(" ")
        pos_depart = configuration.board.position_piece_mat([decision[0][0], decision[0][1]])
        pos_arrivee = configuration.board.position_piece_mat([decision[1][0], decision[1][1]])

        pos_depart = [int(pos) for pos in pos_depart]
        pos_arrivee = [int(pos) for pos in pos_arrivee]

        return [pos_depart, pos_arrivee]


    def en_to_fr(self, fen):
        """
        :param fen str: Composition board en anglais
        :return new_fen_lines list: Composition board en français
        """
        #'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR'
        dic_pieces = {'r' : 't', 'n' : 'c', 'b' : 'f', 'q' : 'd', 'k' : 'r', 'p' : 'p', 'P' : 'P', 'R' : 'T', 'N' : 'C', 'B' : 'F', 'Q' : 'D', 'K' : 'R'}#Traduction pièces anglaises vers pièces françaises
        dic_num = {'1' : 1, '2' : 2, '3' : 3, '4' : 4, '5' : 5, '6' : 6, '7' : 7, '8' : 8}
        fen_lines = fen.split("/")
        new_fen_lines = list()

        for fen_line in fen_lines:
            line = str()
            for piece in fen_line:
                if piece in dic_num.keys():
                    for i in range(0, int(piece)):
                        line += '1'
                elif piece in dic_pieces.keys():
                    line += dic_pieces[piece]
            new_fen_lines.append(line)

        return new_fen_lines


    def fen_to_pos(self, fen):
        """
        :param fen str: Composition board en anglais
        :return pos_pieces: Coordonnées et composition de chaque case de l'échiquier
        """
        board = self.en_to_fr(fen)
        pos_pieces = list()

        cpt_y = 0
        cpt_x = 0 

        line_convert = list()

        for line in board:
            for piece in line:
                if piece != '1' and piece != 'p' and piece != 'P':
                    y = line.index(piece)+1
                    x = board.index(line)+2
                elif len(line) == 8:
                    y = line.index(piece) + cpt_y + 1
                    x = cpt_x+2
                    cpt_y += 1
                else:
                    y = cpt_y + 1
                    x = cpt_x+2
                    cpt_y += 1
                line_convert.append([x, y, piece])
            cpt_y = 0
            cpt_x += 1
            pos_pieces.append(line_convert)
            line_convert = list()

        return pos_pieces


    #avantage joueur, sauvegarde, msg error, promotion, pat
    def game_pvp(self):
        """
        @RG @NR
        """
        configuration = GeneralConf()

        # Crée les joueurs
        configuration.init_joueurs()

    
        init_pieces(configuration)

        # Attribution pièces de chaque joueur
        configuration.pieces_joueurs()


        decision = decision_joueur(input_decision, configuration)
        if self.joueur == 1:
            configuration.deplacement_piece(decision[0], decision[1], True)
        else:
            configuration.deplacement_piece(decision[0], decision[1], False)


        for piece in configuration.pieces_joueurB:
            if piece.get_piece_position()[0] == 2 and piece.nom == 'P' and piece.promotion:
                configuration.promotion(piece)
                piece.promotion = False

        for piece in configuration.pieces_joueurN:
            if piece.get_piece_position()[0] == 9 and piece.nom == 'p' and piece.promotion:
                configuration.promotion(piece)
                piece.promotion = False

        if not len(configuration.msg_error):
            self.joueur = -self.joueur

        configuration.msg_error = list()
