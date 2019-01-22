from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return HttpResponse('<h>hey there!</h>')
# Create your views here.
