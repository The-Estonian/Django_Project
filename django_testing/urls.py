"""django_testing URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
import random
from string import ascii_letters

def randomizer():
    letter_list = list(ascii_letters )
    num_list = list(range(10))
    randomizer_range = letter_list + num_list
    returned_list = []
    for _ in range(30):
        x = str(random.choice(randomizer_range))
        returned_list.append(x)
    returned_list.append("/")
    return "".join(returned_list)
    

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("some_app.urls"))
]
