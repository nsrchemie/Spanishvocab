from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
from collections import defaultdict
import pandas as pd
# Create your views here.

def quiz_render(request):
	r = requests.get('http://lingolex.com/swom/wom-herbs.htm')
	soup = BeautifulSoup(r.content, 'html.parser')
	g_data = [a.text.replace('\n','') for a in soup.find_all('td')]
	iter_data = iter([d for d in g_data[3:] if d.isupper() == False])
	data = defaultdict(list)

	for d in iter_data:
		data[g_data[1]].append(d)
		data[g_data[2]].append(next(iter_data))

	df = pd.DataFrame(data)

	df = df.reset_index().to_json(orient='index')
	return render(request, 'questions/quiz_render.html', {'df':df})