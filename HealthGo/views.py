
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
    querydata = User.objects.all() 

    Users = {
        'Users': querydata
    }
    return render(request, "index.html", Users)


def rewards(request):
        samples = {
            'samples': 'test'
        }

        return render(request, "rewards.html", samples)

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["userid"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "login.html")

        