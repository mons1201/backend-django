from datetime import datetime
from http import client
from django.http import HttpResponse
from django.shortcuts import render
from mongoengine import *
from certifi import *
from . import documents

myCert=where()
client=connect(host="mongodb+srv://mohan:mohan@cluster0.traigro.mongodb.net/?retryWrites=true&w=majority",db="sympoo",username="mohan",password="mohan",tlsCAFile=myCert)


# Create your views here.

def makeCreate(req):
    eve=documents.Event()
    eve.initiate("Sparkers17",datetime.fromisoformat("2022-10-10"),"EEE")
    eve.save()
    return HttpResponse('event has added')

def makeList(req):
    mine=documents.Event.objects.all()
    for x in mine:
        print(x)
    return HttpResponse("Event has listed")
def makePage(req):
    return render(req,'begin.html')
