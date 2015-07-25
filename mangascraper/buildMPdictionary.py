#this is the script used to build mpdict.json
import requests
import bs4
import urllib
import time
url = 'http://www.mangapanda.com/alphabetical'
h = {'User-Agent':'Mozilla/5.0'}
#this dictionary will store information about each manga
mpdict = {}
response = requests.get(url, headers=h)
soup = bs4.BeautifulSoup(response.text)
list = soup.select('ul.series_alpha a')
initiallinks = [i['href'] for i in list]
for j in initiallinks:
	if( j.find('/', 1) + 1): #as if not found it returns -1, so this block below is for manga with id's
		slashpos = j.find('/', 1)
		mangaid = j[1: slashpos:] #this saves the id for that manga if it has one
		manganame = j[slashpos+1:j.find('.',slashpos):]#saves the name of the manga
		mangapage = 'http://www.mangapanda.com'+j #rename mangapage to mangahome cuz it's the homepage of the manga
		try:
			mangapage_response = requests.get(mangapage, headers=h)
			soup = bs4.BeautifulSoup(mangapage_response.text)
			mangalist = soup.select('div#chapterlist a')
			firstchaplink = mangalist[0]['href']
			k = len(mangaid) + 2
			chapterid = firstchaplink[k:firstchaplink.find('-', k):] #that weird unique number mangapanda inserts with first chapter to make scraping harder
			mpdict[manganame] = [mangaid, chapterid]
		except requests.exceptions.ConnectionError:
			mpdict[manganame] = [mangaid, 'error']
		time.sleep(.5)
	else :
		mangaid = '0'
		chapterid = '0'
		manganame = j[1::]
		mpdict[manganame] = [mangaid, chapterid]
		time.sleep(.5)
		

		
		
		
		



