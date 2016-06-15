from bs4 import BeautifulSoup
import requests


r = requests.get('http://lingolex.com/swom/wom-herbs.htm')
soup = BeautifulSoup(r.content, 'html.parser')
g_data = soup.find_all('td')
for a in g_data:
	print(a.text)