from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import messages
import os

from .src.Main_django import Main
from.src.Configuration import GeneralConf

import traceback
import json

from django.contrib.staticfiles.storage import staticfiles_storage

def new_game(request):
	url = os.getcwd() + staticfiles_storage.url('json/save.json')
	try:
		os.remove(url)#réinitialisation de la partie
	except:
		pass#fichier inexistant

	with open(url, 'w') as json_file:
		data = [
				{
					'pos_start': 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR',#Plateau de jeu initial
					'pos_end': None,
					'joueur': 1
				}
			]
		json.dump(data, json_file, indent=3)#création d'un fichier de sauvegarde vierge

	return render(request, 'chessboard.html', {'start': 'False'})


def read_save_and_play(request, main, configuration, save_json):
	######Initialissation des pièces et joueurs
	configuration.init_joueurs()
	main.init_pieces(configuration)
	configuration.pieces_joueurs()

	######Reconstituion des coups joués lors de la partie
	for tour in save_json:
		if tour['pos_end']:
			pos_start = main.fen_to_pos(tour['pos_start'])#Conversion de fen vers matriciel compréhensible par le moteur de jeu
			pos_end = main.fen_to_pos(tour['pos_end'])

			pos_start, pos_end = main.comparaison_coords(pos_start, pos_end)

			main.game_pvp(configuration, pos_start, pos_end, tour['joueur'])

	######Analyse du nouveau coup joué
	oldPos = request.POST['oldPos']
	newPos = request.POST['newPos']

	#Conversion en coordonnées matricielles
	oldPos_convert = main.fen_to_pos(oldPos)
	newPos_convert = main.fen_to_pos(newPos)

	#Comparaison des anciennes positions avec les nouvelles afin de déterminer la pièce à déplacer
	pos_start, pos_end = main.comparaison_coords(oldPos_convert, newPos_convert)

	#Envoi de la décision joueur au moteur de jeu sous forme matricielle
	pos_game = main.game_pvp(configuration, pos_start, pos_end, int(os.environ['JOUEUR']))

	#Conversion position piècs à jour en fen
	return [main.pos_to_fen(pos_game[0]), pos_game[1]]#pos_game[0] -> position des pièces, pos_game[1] -> msg_error


def chessboard(request):
	reset = False

	if not request.POST: #Ouverture de la page de jeu
		os.environ['JOUEUR'] = '1'#joueur blanc

	elif 'btn_new_game'in request.POST:#Réinitialisation du jeu
		reset = True
		new_game(request)

	elif not reset and request.POST:
		main = Main()
		configuration = GeneralConf()

		try:
			url = os.getcwd() + staticfiles_storage.url('json/save.json')
			with open(url) as file:
				save_json = json.load(file)

			play = read_save_and_play(request, main, configuration, save_json)

			if not len(configuration.msg_error):#Coup validé par le moteur de jeu
				main.sauvegarde_partie(url, request.POST['oldPos'], play[0], int(os.environ['JOUEUR']))
				os.environ['JOUEUR'] = str(-int(os.environ['JOUEUR']))

			context = {
				'oldPos': request.POST['oldPos'],
				'new_fen': play[0],
				'msg_error': play[1],
				'avantage': configuration.avantage_joueur(),
				'died_pieces_B': configuration.died_pieces_B,
				'died_pieces_N': configuration.died_pieces_N,
				'joueur': os.environ['JOUEUR'],
				}

			configuration.msg_error = list()

			return render(request, 'chessboard.html', context)

		except Exception:
			#Gère le cas où deux pièces sont jouées ou aucune
			traceback.print_exc()

	#Nouvelle partie ouverture page
	new_game(request)
	return render(request, 'chessboard.html', {'new_fen': 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR'})

def url_pieces_img(request, img):
	return redirect('/static/img/chesspieces/wikipedia/'+img)