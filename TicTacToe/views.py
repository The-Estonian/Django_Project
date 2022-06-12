from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.

def tic_tac_toe(request):
    return render(request, "TicTacToe/tic_tac_toe.html")