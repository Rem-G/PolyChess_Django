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
	'''
	Réinitialise le jeu en supprimant la sauvegarde actuelle et en remettant le joueur à 1
	'''
	os.environ['JOUEUR'] = '1'#joueur blanc
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


def read_save_and_play(request, main, configuration, save_json, url, bot = False):
	'''
	Pour chaque nouveau coup joué, la fonction reconstruit toute la partie à partir du fichier de sauvegarde et envoie le nouveau coup au moteur de jeu
	:param main object: intermédiaire django/moteur de jeu
	:param configuration object: moteur de jeu
	:param save_json dict : sauvegarde de la partie
	'''
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
	pos_game = main.game_pvp(configuration, pos_start, pos_end, 1)

	if bot:
		if not len(pos_game[1]):
			#######Sauvegarde coup joueur accepté
			play = [main.pos_to_fen(pos_game[0]), pos_game[1]]

			main.sauvegarde_partie(url, request.POST['oldPos'], play[0], 1)

			######Tour du bot
			configuration.joueurN.init_bot(configuration)
			error = True

			while error:
				decision_bot = configuration.joueurN.BOT.randomChoice()

				pos_game = main.game_pvp(configuration, decision_bot[0], decision_bot[1], -1)

				if not len(pos_game[1]):
					error = False

				configuration.msg_error = list()

			return [main.pos_to_fen(pos_game[0]), pos_game[1], play[0]]


	#Conversion position pièces à jour en fen
	return [main.pos_to_fen(pos_game[0]), pos_game[1]]#pos_game[0] -> position des pièces, pos_game[1] -> msg_error


def chessboard(request):
	'''
	Analyse les éléments POST du template et les envoie au moteur de jeu
	'''
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
			play = read_save_and_play(request, main, configuration, save_json, url)

			if not len(play[1]):#Coup validé par le moteur de jeu, pas d'erreur
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
			#traceback.print_exc()
			pass

	#Nouvelle partie/ouverture page
	new_game(request)
	return render(request, 'chessboard.html', {'new_fen': 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR'})


def chessboard_bot(request):
	'''
	Analyse les éléments POST du template et les envoie au moteur de jeu
	'''
	reset = False

	if not request.POST: #Ouverture de la page de jeu
		os.environ['JOUEUR'] = '1'#joueur blanc

	elif 'btn_new_game'in request.POST:#Réinitialisation du jeu
		reset = True
		new_game(request)

	elif not reset and request.POST:
		print(request.POST)
		main = Main()
		configuration = GeneralConf()

		try:
			url = os.getcwd() + staticfiles_storage.url('json/save.json')
			with open(url) as file:
				save_json = json.load(file)

			play = read_save_and_play(request, main, configuration, save_json, url, True)

			oldPos = request.POST['oldPos']

			if not len(play[1]):#Coup validé par le moteur de jeu, pas d'erreur
				#Sauvegarde coup bot
				if play[2]:
					oldPos = play[2]
					main.sauvegarde_partie(url, oldPos, play[0], -1)
				else:
					main.sauvegarde_partie(url, oldPos, play[0], -1)

			context = {
				'oldPos': oldPos,
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
			#pass

	#Nouvelle partie/ouverture page
	new_game(request)
	return render(request, 'chessboard.html', {'new_fen': 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR'})

def url_pieces_img(request, img):
	'''
	Redirection des url d'images du plateau de jeu de chessboard.js
	'''
	return redirect('/static/img/chesspieces/wikipedia/'+img)

