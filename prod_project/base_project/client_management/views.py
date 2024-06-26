from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.db.utils import OperationalError
from django.db import connections

def index(request):
    return render(request, 'index.html')