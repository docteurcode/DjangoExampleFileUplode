from django.shortcuts import render
from . import models

def index_view(request):
	if request.POST:
		file = models.FileUplode()
		file.file = request.FILES['file']
		file.save()
	return render(request, 'index.html', {})
