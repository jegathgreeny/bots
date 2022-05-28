import requests
from bs4 import BeautifulSoup
import webbrowser


# The default address that is same for all movies.
site = 'https://yts.mx/movies/'


with open(r'C:\Users\jegat\Desktop\py_work\work\bots\link_generator\selected.txt', 'r') as selected_films:
	for film in selected_films:
		# Strip the movie string of whitespaces.
		film = film.strip()
		try:
			res = requests.get(f'{site}{film}')
			res.raise_for_status()

			# 'lxml' is faster than 'html.parser'.
			soup = BeautifulSoup(res.text, 'lxml')
			links = soup.select('p > a[rel="nofollow"]')

			# Break out of the loop with their is a match.
			# The if statements are placed in this order so that 720p if available will be downloaded first.
			for link in links:
				if '720p.BluRay' in link: 
					webbrowser.open(link.get('href'))
					break
				elif '720p.WEB' in link:
					webbrowser.open(link.get('href'))
					break
				elif '1080p.BluRay' in link:
					webbrowser.open(link.get('href'))
					break
				elif '1080p.WEB' in link:
					webbrowser.open(link.get('href'))
					break
		except:
			# If the movie is not found browse via pirate bay.
			print(f'browsing {film}via piratebay...')
			webbrowser.open(f'https://thepiratebay.org/search.php?q={film}&all=on&search=Pirate+Search&page=0&orderby=')
		else:
			# Tell the user the yts being used.
			print(f'Downloading {film} via yts')
