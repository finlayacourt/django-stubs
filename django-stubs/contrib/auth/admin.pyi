from typing import Any, TypeVar

from django.contrib import admin
from django.contrib.auth.models import AbstractBaseUser, Group
from django.http.request import HttpRequest
from django.http.response import HttpResponse

_AbstractUserT = TypeVar("_AbstractUserT", bound=AbstractBaseUser)

class GroupAdmin(admin.ModelAdmin[Group]): ...

class UserAdmin(admin.ModelAdmin[_AbstractUserT]):
    change_user_password_template: Any
    add_fieldsets: Any
    add_form: Any
    change_password_form: Any
    def user_change_password(self, request: HttpRequest, id: str, form_url: str = ...) -> HttpResponse: ...
