from random import shuffle

from django.shortcuts import render
from .models import ToDoList
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def base_template(request):
    return render(request, "some_app/base_template.html")


def index(request):
    return render(request, "some_app/index.html")


def sign_up(request):
    if request.method == "POST":
        username = request.POST.dict()["username"]
        password = request.POST.dict()["password"]
        email = request.POST.dict()["email"]
        first_name = request.POST.dict()["first_name"]
        last_name =request.POST.dict()["last_name"]
        new_user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
        new_user.save()
    else:
        pass
    return render(request, "some_app/sign_up.html")
    

def show_data(request):
    if request.method == "POST":
        id_to_delete = request.POST.dict()["id_to_delete"]
        User.objects.filter(id=id_to_delete).delete()
    all_users = User.objects.values()
    context = {"all_users":all_users}
    return render(request, "some_app/show_data.html", context)

def tic_tac_toe(request):
    return render(request, "some_app/tic_tac_toe.html")
    

def login_page(request):
    if request.method == "POST":
        username = request.POST.dict()["username"]
        password = request.POST.dict()["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, "some_app/index.html")
        else:
            context = {"password":"Password incorrect!"}
            return render(request, "some_app/login_page.html", context)
    else:
        return render(request, "some_app/login_page.html")


def log_out(request):
    logout(request)
    return render(request, "some_app/index.html")

@login_required(login_url="login_page")
def to_do_list(request):
    to_do_user = request.user.id
    to_do_list = ToDoList.objects.filter(user_id=to_do_user).order_by('?')
    context = {"to_do_list" : to_do_list}
    if request.method == "POST":
        id_to_delete = request.POST.dict()["id_to_delete"]
        ToDoList.objects.filter(id=id_to_delete).delete()
        return render(request, "some_app/to_do_list.html", context)
    else:
        return render(request, "some_app/to_do_list.html", context)



    # def login_page(request):
    #     if request.method == "POST":
    #         username = request.POST.dict()["username"]
    #         password = request.POST.dict()["password"]
    #         user = SignUp.objects.filter(username=username).values()
    #         if user[0]["password"] == password:
    #             SiteTemplate.context["login"] = user[0]["username"]
    #     return render(request, "some_app/login_page.html", SiteTemplate.context)

    # def login_page(request):
    #     if request.method == "POST":
    #         username = request.POST.dict()["username"]
    #         password = request.POST.dict()["password"]
    #         email = request.POST.dict()["email"]
    #         first_name = request.POST.dict()["first_name"]
    #         last_name =request.POST.dict()["last_name"]
    #         new_sign = SignUp(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
    #         new_sign.save()
    #     else:
    #         pass
        
    #     return render(request, "some_app/sign_up.html", SiteTemplate.context)