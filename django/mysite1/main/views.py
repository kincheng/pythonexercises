from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def homepage(request):
	return HttpResponse('this is an awesome page <strong>number 2!</strong>')