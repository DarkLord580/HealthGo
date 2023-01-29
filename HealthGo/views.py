
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import *

from django.http import JsonResponse
from django.template import Context, loader
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
import json
from datetime import datetime
import pytz



def index(request):

    if "uid" in request.session:
        uid = request.session['uid']
        user = User.objects.get(id=uid)
        
        if user is not None:
            loginuser = {
                'loginuser': user
            }
            return render(request, "index.html", loginuser)
    return render(request, "index.html")


def rewards(request):
        samples = {
            'samples': 'test'
        }

        return render(request, "rewards.html", samples)

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]

        print("######################")
        print("user", username)
        print("######################")

        loginuser = User.objects.filter(username=username)
        
        print("login user", loginuser)
        
        if loginuser is not None and len(loginuser) is not 0  and password == loginuser[0].password:
                request.session['uid'] = loginuser[0].id
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

        
