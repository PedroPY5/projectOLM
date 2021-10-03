from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
#from . forms import UserRegisterForm

def index(request):

    return render(request, 'index.html')
def reg(request):
    pass


