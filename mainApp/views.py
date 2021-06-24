from django.shortcuts import render
from django.http import HttpResponse

#default view
def index(request):
    return HttpResponse("Hello world! This is the myChores placeholder page!")