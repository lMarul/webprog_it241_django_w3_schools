from django.shortcuts import render
from django.http import HttpResponse

def members(request):
    return HttpResponse(" <b>Hello WEBPROG IT241 world!</b>")