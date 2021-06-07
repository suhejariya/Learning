from django.shortcuts import render
from django.http.response import HttpResponse
from .models import QuesAns
from django.core import serializers
from django.http import JsonResponse
# Create your views here.
def myview(request):
    QuesAns.objects.create(ques="hello" , ans="what???")
    ans =  QuesAns.objects.all()
    return JsonResponse(serializers.serialize('json', ans), safe=False)