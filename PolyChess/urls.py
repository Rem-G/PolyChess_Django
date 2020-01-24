from django.urls import path, re_path
from django.conf.urls import url
from . import views

app_name = 'polychess'

urlpatterns = [
	url(r'^$', views.chessboard, name='chessboard'),
	url(r'bot$', views.chessboard_bot, name='chessboard_bot'),
	url(r'img/chesspieces/wikipedia/(?P<img>[A-z.]+)$', views.url_pieces_img, name='url_pieces_img'),
]