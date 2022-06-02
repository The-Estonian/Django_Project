from django.contrib import admin
from django.urls import path, include
from .views import user_accounts

urlpatterns = [
    path("", user_accounts, name="user_accounts")
]
