'''
Projet PolyChess - PROJ531
VIEU Loïc
CENCI Thomas
RAZAFINDRABE Noah
GOSSELIN Rémi
'''
from .Configuration import *
import traceback
import json
import os

class Main():
    def __init__(self):
        pass

    def init_pieces(self, configuration):
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


    def fen_to_list(self, fen):
        """
        Conversion coordonnées fen en liste de pièces
        :param fen str: Composition board
        :return new_fen_lines list: Liste de pièces
        """
        #'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR'
        fen_lines = fen.split("/")
        new_fen_lines = list()

        for fen_line in fen_lines:
            line = str()
            for piece in fen_line:
                if piece in ['1', '2', '3', '4', '5', '6', '7', '8']:
                    for i in range(0, int(piece)):
                        line += '1'
                else:
                    line += piece
            new_fen_lines.append(line)

        return new_fen_lines


    def fr_to_en(self, pos):
        """
        Conversion des noms de pièces du français à l'anglais
        :param pos list:
        :return pos list:
        """
        dic_pieces = {'t' : 'r', 'c' : 'n', 'f' : 'b', 'd' : 'q', 'r' : 'k', 'p' : 'p', 'P' : 'P', 'T' : 'R', 'C' : 'N', 'F' : 'B', 'D' : 'Q', 'R' : 'K'}#Traduction pièces anglaises vers pièces françaises
        for piece in pos:
            pos[pos.index(piece)][1] = dic_pieces[piece[1]]
        return pos


    def fen_to_pos(self, fen):
        """
        Conversion fen en coordonnées matricielles
        :param fen str: Composition board en anglais
        :return pos_pieces: Coordonnées et composition de chaque case de l'échiquier
        """

        board = self.fen_to_list(fen)
        pos_pieces = list()

        cpt_y = 0
        cpt_x = 0 

        line_convert = list()

        for line in board:#liste des lignes
            for piece in line:#pièces de la ligne
                y = cpt_y + 1
                x = cpt_x + 2

                cpt_y += 1#parcours la ligne

                line_convert.append([x, y, piece])

            cpt_y = 0
            cpt_x += 1#parcours la colonne

            pos_pieces.append(line_convert)
            line_convert = list()

        return pos_pieces


    def pos_to_fen(self, pos):
        """
        Conversion coordonnées matricieelles en coordonnées fen
        :param pos list: coordonnées matricielles des pièces
        :return fen str: coordonnées des pièces en fen
        """

        pos = self.fr_to_en(pos)#conversion pièces fr en anglais afin d'être lisibles par le board du template
        fen = str()

        for i in range(2,10):#lignes du plateau
            line_list = ['1', '1','1', '1','1', '1','1', '1']
            line_str = str()
            for j in range(1,9):#colonnes plateau
                for piece in pos:
                    if piece[0] == [i,j]:
                        line_list[j-1] = piece[1]#-1 -> premier index de liste = 0
            for element in line_list:
                line_str += element
            fen += line_str + '/'

        return fen[:len(fen)-1]#retire le dernier /

    def comparaison_coords(self, oldPos, newPos):
        """
        Comparaison des coordonnées entre le board avant coup et board après coup
        Permet de récupérer la position de départ et d'arrivée du coup joué
        :param oldPos list: board initial
        :param newPos list: board après coup
        :return list: position de départ du coup joué, position d'arrivée du coup joué
        """
        pos_depart = None
        pos_arrivee = None

        for line in range(0,8):
            if newPos[line] != oldPos[line]:
                for piece in range(0,8):
                    if newPos[line][piece] != oldPos[line][piece] and newPos[line][piece][2] != oldPos[line][piece][2]:#A un emplacement donné, coordonnées pièce différentes et pièces différentes à cet emplacement
                        if newPos[line][piece][2] == '1':#Si une pièce a été bougé, sa position initiale devient 1
                            pos_depart = newPos[line][piece][:2]
                        else:
                            pos_arrivee = newPos[line][piece][:2]


        return [pos_depart, pos_arrivee]

    def sauvegarde_partie(self, path, oldPos, newPos, joueur):
        """
        Sauvegarde chaque coup joué dans un fichier json
        :param path str: chemin du fichier de sauvegarde
        :oldPos str: composition ancien board en fen
        :newPos str: composition nouveau board en fen
        :joueur str: 1 ou -1, joueur qui a joué
        """
        with open(path, 'r') as json_file:
            data = json.load(json_file)#Récupère le fichier

        data.append({'pos_start': oldPos, 'pos_end': newPos, 'joueur': joueur})

        with open(path, 'w') as json_file:
            json.dump(data, json_file, indent=3)


    def game_pvp(self, configuration, pos_depart, pos_arrivee, joueur):
        """
        Envoie la décision du joueur au moteur de jeu, gère la promotion

        :param configuration object: moteur de jeu
        :param pos_depart list: position de départ du coup joué
        :param pos_arrivee list: position d'arrivée du coup joué
        :joueur int: joueur qui a joué le coup
        :return list: renvoie la position de chaque pièce et les messages d'erreur
        """
        if joueur == 1:
            configuration.deplacement_piece(pos_depart, pos_arrivee, True)
        else:
            configuration.deplacement_piece(pos_depart, pos_arrivee, False)

        for piece in configuration.pieces_joueurB:
            if piece.get_piece_position()[0] == 2 and piece.nom == 'P' and piece.promotion:
                configuration.promotion(piece)
                piece.promotion = False

        for piece in configuration.pieces_joueurN:
            if piece.get_piece_position()[0] == 9 and piece.nom == 'p' and piece.promotion:
                configuration.promotion(piece)
                piece.promotion = False

        positions = list()
        positions = [[piece.position, piece.nom] for piece in configuration.pieces]
        
        return [positions, configuration.msg_error]
