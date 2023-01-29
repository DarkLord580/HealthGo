
from django.contrib.auth import  login,logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from HealthGo.models import User

from django.http import JsonResponse
from django.template import Context, loader
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
import json
from datetime import datetime
import pytz



def index(request):

    if "un" in request.session:
        username = request.session['un']
        user = User.objects.get(username=username)
        
        if user is not None:
            loginuser = {
                'loginuser': user
            }
            return render(request, "index.html", loginuser)
    return render(request, "index.html")


def rewards(request):
    if "un" in request.session:
        username = request.session['un']
        user = User.objects.get(username=username)
        if user is not None:
            winners = User.objects.all()
            print("winner==========", winners)
            loginuser = {
                'loginuser': user ,
                'winners' :winners
            }
        
            return render(request, "rewards.html", loginuser)
    return render(request, "login.html")

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]

        loginuser = User.objects.filter(username__iexact=username)
        print ("loginuser=", loginuser )
        
        if loginuser is not None and len(loginuser) is not 0  and password == loginuser[0].password:
                request.session['un'] = loginuser[0].username
                login(request, loginuser[0])
                return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "login.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))



        
