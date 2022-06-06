from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.
def user_accounts(request):
    current_user_id = request.user.id
    current_user = User.objects.filter(id = current_user_id).values()
    user_instance = User.objects.get(id = current_user_id)
    context = {"current_user":current_user}
    if request.method == "POST":
        new_username = request.POST.dict()["username"]
        old_password = request.POST.dict()["old-password"]
        new_password = request.POST.dict()["new-password"]
        new2_password = request.POST.dict()["new2-password"]
        email = request.POST.dict()["email"]
        first_name = request.POST.dict()["first-name"]
        last_name = request.POST.dict()["last-name"]
        # print(current_user)
        # print(user_instance)
        # print(request.POST)
        if len(new_username) > 0:
            user_instance.username = new_username
            user_instance.save()
            context = {"current_user":current_user, "user":user_instance}
            return render(request, "accounts/account_page.html", context)
        elif len(old_password) > 0:
            if user_instance.check_password(old_password) and new_password == new2_password:
                user_instance.set_password(new_password)
                user_instance.save()
                print(user_instance.password)
            return render(request, "accounts/account_page.html", context)
        elif len(email) > 0:
            user_instance.email = email
            user_instance.save()
            return render(request, "accounts/account_page.html", context)
        elif len(first_name) > 0:
            user_instance.first_name = first_name
            user_instance.save()
            return render(request, "accounts/account_page.html", context)
        elif len(last_name) > 0:
            user_instance.last_name = last_name
            user_instance.save()
            return render(request, "accounts/account_page.html", context)
        else:
            # current_user_instance = User.objects.filter(id = current_user_id).values()
            # context = {"current_user":current_user_instance}
            # print(user_instance)
            return render(request, "accounts/account_page.html", context)
    else:
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

    <QueryDict: 
    {'csrfmiddlewaretoken': ['ES2g0pJoI1tYoyjZCCU9DHwqUP44oqOcug0lyWc250XTSQob4PJ5uqNlENfGWt81'], 
    'username': ['Arno'], 
    'old-password': [''], 
    'new-password': [''], 
    'new2-password': [''], 
    'email': [''], 
    'first_name': [''], 
    'last_name': ['']}>
"""