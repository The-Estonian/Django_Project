from django.contrib import admin
from django.urls import path, include
from .views import tic_tac_toe

urlpatterns = [
    path("", tic_tac_toe, name="tic_tac_toe")
]
