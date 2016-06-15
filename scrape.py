from bs4 import BeautifulSoup
import requests


r = requests.get('http://lingolex.com/swom/wom-herbs.htm')
soup = BeautifulSoup(r.content, 'html.parser')
g_data = [a.text for a in soup.find_all('td')]
g_data = iter([d for d in g_data[1:] if d.isupper() == False])
for d in g_data:
		print(' Spanish: ',d, '\n', 'English: ', next(g_data), '\n')