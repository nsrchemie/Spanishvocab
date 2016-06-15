from bs4 import BeautifulSoup
import requests
from collections import defaultdict
import pandas as pd


r = requests.get('http://lingolex.com/swom/wom-herbs.htm')
soup = BeautifulSoup(r.content, 'html.parser')
g_data = [a.text for a in soup.find_all('td')]
iter_data = iter([d for d in g_data[3:] if d.isupper() == False])
# col1 = g_data[1]
# col2 = g_data[2]
# for d in g_data:
# 		print(' Spanish: ',d, '\n', 'English: ', next(g_data), '\n')
data = defaultdict(list)

for d in iter_data:
	data[g_data[1]].append(d)
	data[g_data[2]].append(next(iter_data))

df = pd.DataFrame(data)

print(df.head())




