from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

from .models import Employee
from .forms import EmployeeChangeForm, EmployeeCreationForm

class EmployeeAdmin(UserAdmin):

    add_form = EmployeeCreationForm
    form = EmployeeChangeForm
    model = Employee
    list_display = ['email', 'username']

admin.site.register(Employee, EmployeeAdmin)