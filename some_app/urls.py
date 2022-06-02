from django.urls import path, include

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
    path('login_page/', login_page, name='login_page'),
    path('log_out/', log_out, name='log_out'),
    path('tic_tac_toe/', include("TicTacToe.urls")),
    path("accounts/", include("accounts.urls"))
]
