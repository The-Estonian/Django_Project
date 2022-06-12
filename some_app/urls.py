from django.urls import path, include
import random
from string import ascii_letters

def randomizer():
    letter_list = list(ascii_letters )
    num_list = list(range(10))
    randomizer_range = letter_list + num_list
    returned_list = []
    for _ in range(50):
        x = str(random.choice(randomizer_range))
        returned_list.append(x)
    returned_list.append("/")
    return "".join(returned_list)
    

from .views import (
    index,
    sign_up,
    show_data,
    to_do_list,
    login_page,
    log_out
)


urlpatterns = [
    path('', index, name='front_page'),
    path('sign_up/', sign_up, name='sign_up'),
    path("show_data/", show_data, name="show_data"),
    path('to_do_list/', to_do_list, name='To-Do-List'),
    path(randomizer(), to_do_list, name='To-Do-List'),
    path('login_page/', login_page, name='login_page'),
    path('log_out/', log_out, name='log_out'),
    path('tic_tac_toe/', include("TicTacToe.urls")),
    path("accounts/", include("accounts.urls"))
]
