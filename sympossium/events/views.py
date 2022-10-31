from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.decorators.cache import cache_control
from mongoengine import *
from certifi import *
from . import documents

myCert=where()
client=connect(host="mongodb+srv://mohan:mohan@cluster0.traigro.mongodb.net/?retryWrites=true&w=majority",db="sympoo",username="mohan",password="mohan",tlsCAFile=myCert)


# Create your views here.
@cache_control(no_cache=True,no_store=True,must_revalidate=True,expires=0)
def makeLogout(req):
    if req.session.has_key('person'):
        req.session['person']=""
        del req.session['person']
    return redirect('/buddy/')

@cache_control(no_cache=True,no_store=True,must_revalidate=True,expires=0)
def makeLogin(req):
    if req.method=="POST":
        a=req.POST['username']
        b=req.POST['password']
        if a=="mohana" and b=="mohan":
            req.session['person']=a
            return redirect('/buddy/home')
        else:
            return redirect('/buddy/')
    else:
        return render(req,'index.html')

@cache_control(no_cache=True,no_store=True,must_revalidate=True,expires=0)
def makeShort(req):
    if req.session.has_key('person'):
        if req.method=="POST":
            first=req.POST['dept']
            second=req.POST['date']
            if first=="select Department":
                objs=documents.Event.objects(eveDate=second)
            else:
                objs=documents.Event.objects(eveDepartment=first)
            return render(req,'viewing.html',{"everything":objs})
        else:
            return render(req,'short.html')
    else:
        return redirect('/buddy/')

@cache_control(no_cache=True,no_store=True,must_revalidate=True,expires=0)
def makeAnnounce(req,key,name):
    if req.session.has_key('person'):
        documents.Event.objects(eveId=key).update_one(set__eveWinner=name)
        return redirect("/buddy/home")
    else:
        return redirect('/buddy/')

@cache_control(no_cache=True,no_store=True,must_revalidate=True,expires=0)
def makeRemove(req,key,name):
    if req.session.has_key('person'):
        documents.Event.objects(eveId=key).update_one(pull__eveParticipants=name)
        return redirect('/buddy/home')
    else:
        return redirect('/buddy/')

@cache_control(no_cache=True,no_store=True,must_revalidate=True,expires=0)
def makeAddParts(req,pos):
    if req.session.has_key('person'):
        if req.method=="POST":
            eid=req.POST['eveid']
            part=req.POST['person']
            documents.Event.objects(eveId=eid).update_one(push__eveParticipants=part)
            return redirect('/buddy/home')
        else:
            receive=documents.Event.objects(eveId=pos).first()
            return render(req,'enroll.html',{"ondru":receive})
    else:
        return redirect('/buddy/')

@cache_control(no_cache=True,no_store=True,must_revalidate=True,expires=0)
def makeViewParts(req,key):
    if req.session.has_key('person'):
        receive=documents.Event.objects(eveId=key).first()
        return render(req,'people.html',{"all":receive})
    else:
        return redirect('/buddy/')

@cache_control(no_cache=True,no_store=True,must_revalidate=True,expires=0)
def makeDelete(req,unique):
    if req.session.has_key('person'):
        receive=documents.Event.objects(eveId=unique).first()
        receive.delete()
        return redirect('/buddy/home')
    else:
        return redirect('/buddy/')

@cache_control(no_cache=True,no_store=True,must_revalidate=True,expires=0)
def makeEdit(req,num):
    if req.session.has_key('person'):
        if req.method=="POST":
            d=req.POST['eveid']
            nm=req.POST['evename']
            dt=req.POST['evedate']
            dp=req.POST['evedept']
            documents.Event.objects(eveId=d).update_one(set__eveName=nm,set__eveDate=dt,set__eveDepartment=dp)
            return redirect('/buddy/home')
        else:
            receive=documents.Event.objects(eveId=num).first()
            return render(req,'edit.html',{"record":receive})
    else:
        return redirect('/buddy/')

@cache_control(no_cache=True,no_store=True,must_revalidate=True,expires=0)
def makeRead(req,seriel):
    if req.session.has_key('person'):
        receive=documents.Event.objects(eveId=seriel).first()
        return render(req,'one.html',{"data":receive})
    else:
        return redirect('/buddy/')


@cache_control(no_cache=True,no_store=True,must_revalidate=True,expires=0)
def makeCreate(req):
    if req.session.has_key('person'):
        if req.method=="POST":
            #print("POST accepted")
            nm=req.POST['evename']
            dt=req.POST['evedate']
            dp=req.POST['evedept']
            #print(nm,dt,dp)
            eve=documents.Event()
            eve.initiate(nm,datetime.fromisoformat(dt),dp)
            eve.save()
            return render(req,'schedule.html',{"info":nm+ "has scheduled" })
        else:
            return render(req,'schedule.html')
    else:
        return redirect('/buddy/')

    '''eve=documents.Event()
    eve.initiate("Sparkers17",datetime.fromisoformat("2022-10-10"),"EEE")
    eve.save()
    return HttpResponse('event has added')
'''
@cache_control(no_cache=True,no_store=True,must_revalidate=True,expires=0)
def makeList(req):
    if req.session.has_key('person'):
        mine=documents.Event.objects.all()
        # for x in mine:print(x)
        # # return HttpResponse("Event has listed")
        return render(req,'viewing.html',{"everything":mine})
    else:
        return redirect('/buddy/')
def makePage(req):
    return render(req,'begin.html')
