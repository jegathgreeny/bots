import requests, bs4
import os, csv
import threading


def single_genre(url, genre):
	'''Downloads data from a single genre.'''
	while not url.endswith('#'):
		res = requests.get(url)
		res.raise_for_status()
		
		# parses
		soup = bs4.BeautifulSoup(res.text, 'lxml')

		# Select the single tab.
		wholeElem = soup.select('.lister-item')

		os.makedirs('imdb_data', exist_ok=True)
		with open(os.path.join('imdb_data', f'{genre}.csv'), 'a', newline='') as outputFile:
			outputWriter = csv.writer(outputFile)
			for i in range(len(wholeElem)):

				# Stores a single movie's data.
				movie = wholeElem[i].text.split('\n')
				try:
					title = movie[10]
					year = ''.join(chara for chara in movie[11] if chara.isdigit())
					rating = float(movie[24])
					# If the rating is greater than 6.4, add title to the csv file.
					if rating >= 6.6:
						outputWriter.writerow([title, year, rating])
				except:
					with open(os.path.join('imdb_data', 'upcoming_films.txt'), 'a') as textFile:
						textFile.write(f'{title} {year}\n')

		nextLink = soup.select('.next-page')[0]
		url = 'https://imdb.com' + nextLink.get('href')


genres = ['comedy', 'scifi', 'horror', 'romance', 'action', 'thriller', 'drama', 'mystery', 'crime', 'animation', 'adventure', 'fantasy', 'comedy,romance', 'action,comedy', 'superhero']

genre_threads = []
# Loop over all the genres.
for genre in genres:
	print(f'scraping {genre} films...')
	genre_url = f'https://www.imdb.com/search/title/?genres={genre}&explore=title_type,genres&title_type=movie&ref_=adv_explore_rhs'

	# To scrape each genre of data seperately.
	genre_thread = threading.Thread(target=single_genre, args=(genre_url,genre,))
	genre_threads.append(genre_thread)
	genre_thread.start()

# This waits for all threads to finish.
for genre_thread in genre_threads:
	genre_thread.join()

print('Done.')