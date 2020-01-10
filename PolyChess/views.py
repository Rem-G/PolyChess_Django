from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import messages

from .src.Main_django import Main

import traceback

def comparaison_coords(oldPos, newPos):
	"""
	"""
	pos_depart = None
	pos_arrivee = None

	for line in range(0,8):
		if newPos[line] != oldPos[line]:
			for piece in range(0,8):
				if newPos[line][piece] != oldPos[line][piece] and newPos[line][piece][2] != oldPos[line][piece][2]:
					if newPos[line][piece][2] == '1':
						pos_depart = newPos[line][piece][:2]
					else:
						pos_arrivee = newPos[line][piece][:2]


	return [pos_depart, pos_arrivee]

def chessboard(request):
	start = 'False'
	if request.POST:
		start = 'True'
		main  = Main()
		print(request.POST)
		try:
			oldPos = request.POST['oldPos']
			newPos = request.POST['newPos']

			oldPos_convert = main.fen_to_pos(oldPos)
			newPos_convert = main.fen_to_pos(newPos)

			pos_start, pos_end = comparaison_coords(oldPos_convert, newPos_convert)

			print(pos_start, pos_end)

			#return HttpResponse(pos_start, pos_end)
		except Exception:
			traceback.print_exc()#Ajouter message erreur 'jouer une pièce'
		

	return render(request, 'chessboard.html', locals())

def url_pieces_img(request, img):
	return redirect('/static/img/chesspieces/wikipedia/'+img)