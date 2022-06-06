from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.
def tic_tac_toe(request):
    # current_user_id = request.user.id
    # current_user = User.objects.get(id = current_user_id)
    # # print(current_user)
    # username = current_user.username
    # password = current_user.password
    # user = authenticate(request, username=username, password=password)
    # if user is not None:
    #         login(request, user)
    # print(user)
    return render(request, "TicTacToe/tic_tac_toe.html")