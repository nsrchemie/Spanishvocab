from django.shortcuts import render

# Create your views here.

def quiz_render(request):
	return render(request, 'questions/quiz_render.html', {})