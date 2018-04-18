import requests
from bs4 import BeautifulSoup
from random import randint

def get_poem(count = 0):
	max_pages = 855

	page_number = randint(1, 855)

	headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

	page = requests.get('https://www.poetryfoundation.org/ajax/poems?page=' + str(page_number) + '&sort_by=recently_added', headers=headers)

	poems = page.json()['Entries']

	poem_data = poems[randint(0, len(poems))]

	poem_title = BeautifulSoup(poem_data['title'], 'html.parser').get_text()
	poem_author = BeautifulSoup(poem_data['author'], 'html.parser').get_text()
	poem_link = poem_data['link']

	poem_page = BeautifulSoup(requests.get(poem_link, headers=headers).content, 'html.parser')

	poem_content = poem_page.find('div', {'class':'o-poem'})

	try:
		poem = poem_title + '\n' + poem_author + '\n'
		for d in poem_content.find_all('div'):
			poem += '\n' + d.get_text()
		return poem
	except:
		if count < 3:
			return get_poem(count+1)
		else:
			return None