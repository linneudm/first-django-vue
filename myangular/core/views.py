from django.shortcuts import render, get_object_or_404
from django.core import serializers
from django.http import JsonResponse
# Create your views here.
from .models import Agenda

# Página inicial

def index(request):
	
	agenda = Agenda.objects.all()
	context = {
		'agenda_list': agenda,
	}
	
	return render(request, 'index.html', context)

