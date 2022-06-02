from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.
def user_accounts(request):
    current_user_id = request.user.id
    current_user = User.objects.filter(id = current_user_id).values()
    print(current_user)
    context = {"current_user":current_user}
    return render(request, "accounts/account_page.html", context)


"""
<QuerySet [
    {'id': 3, 
    'username': 'Third_user', 
    'first_name': 'Third', 
    'last_name': 'User', 
    'email': 'Third@user.com', 
    'is_active': True, 
    'is_staff': False, 
    'is_superuser': False, 
    'last_login': datetime.datetime(2022, 6, 2, 20, 7, 9, 447758, tzinfo=datetime.timezone.utc), 
    'date_joined': datetime.datetime(2022, 5, 28, 20, 16, 58, 975808, tzinfo=datetime.timezone.utc)}]>
"""