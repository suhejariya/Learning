from django.shortcuts import render
from django.http.response import HttpResponse
# Create your views here.
def myview(request):
    return HttpResponse('hello welcome riya')