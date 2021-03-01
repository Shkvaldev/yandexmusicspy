import requests
import json
from bs4 import BeautifulSoup

def parser_fav(page, login):
	template = BeautifulSoup(page, "html.parser")
	ans = template.get_text()
	ans = ans.split("   ")
	new_text = str(ans[1])
	result = new_text.split(login)
	return result[0]

def favorite(login):
	url = "https://music.yandex.com/users/{}/playlists/3".format(str(login))
	req = requests.get(url)
	if req.status_code != 200:
		return '''Данного пользователя не существует :(
		 *попробуйте помениять логин на электронную почту (если таковая имеется)'''
	else:
		text = parser_fav(req.text, login)
		return "Пользователю нравятся следующие произведения:\n"+text


def playlists(login):
	pass 