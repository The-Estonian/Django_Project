from django.contrib import admin

# Register your models here.
from .models import ToDoList, DoneOrNot

admin.site.register(ToDoList)
admin.site.register(DoneOrNot)
