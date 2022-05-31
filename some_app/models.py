from django.db.models import Model, CharField, DateTimeField, EmailField, ForeignKey, RESTRICT
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User

# Create your models here.


# class SignUp(Model):
#     username = CharField(max_length=50, blank=False, null=False, unique=True, validators=[MinLengthValidator(4)])
#     password = CharField(max_length=50, blank=False, null=False, validators=[MinLengthValidator(6)])
#     email = EmailField(unique=True)
#     first_name = CharField(max_length=50, blank=False, null=False, validators=[MinLengthValidator(4)])
#     last_name = CharField(max_length=50, blank=False, null=False, validators=[MinLengthValidator(4)])
#     timestamp = DateTimeField(auto_now_add=True, auto_now=False)
#     updated = DateTimeField(auto_now_add=False, auto_now=True)
    
#     def __str__(self):
#         return self.username


# class Player_choice(Model):
#     player = CharField(max_length=50, unique=True)

#     def __str__(self):
#         return self.player



# class Grid_choice(Model):
#     username = ForeignKey(SignUp, on_delete=RESTRICT)
#     player = ForeignKey(Player_choice, on_delete=RESTRICT)
#     grid_choice1 = CharField(max_length=5)
#     grid_choice2 = CharField(max_length=5)
#     grid_choice3 = CharField(max_length=5)
#     grid_choice4 = CharField(max_length=5)
#     grid_choice5 = CharField(max_length=5)
#     grid_choice6 = CharField(max_length=5)
#     grid_choice7 = CharField(max_length=5)
#     grid_choice8 = CharField(max_length=5)
#     grid_choice9 = CharField(max_length=5)
#     timestamp = DateTimeField(auto_now_add=True, auto_now=False)

#     class Meta:
#         unique_together = (("grid_choice1", "grid_choice2"),)

class DoneOrNot(Model):
    done_or_not = CharField(max_length=50)

    def __str__(self):
        return self.done_or_not

class ToDoList(Model):
    user_id = ForeignKey(User, on_delete=RESTRICT)
    to_do_message = CharField(max_length=80)
    done_or_not = ForeignKey(DoneOrNot, on_delete=RESTRICT, default=2)

    def __str__(self):
        return self.to_do_message[:30]
