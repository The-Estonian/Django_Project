from django.db.models import Model, CharField, DateTimeField, EmailField, ForeignKey, RESTRICT, CASCADE
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User


class DoneOrNot(Model):
    done_or_not = CharField(max_length=50)

    def __str__(self):
        return self.done_or_not


class ToDoList(Model):
    user_id = ForeignKey(User, on_delete=CASCADE)
    to_do_message = CharField(max_length=20)
    done_or_not = ForeignKey(DoneOrNot, on_delete=CASCADE, default=1)

    def __str__(self):
        return  f"{str(self.user_id)} -> {str(self.to_do_message)} -> {str(self.done_or_not)}"


