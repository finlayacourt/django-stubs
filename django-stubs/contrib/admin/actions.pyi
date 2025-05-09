from typing import Any

from django.contrib.admin.options import ModelAdmin
from django.db.models.query import QuerySet
from django.http.request import HttpRequestUser
from django.template.response import TemplateResponse

def delete_selected(
    modeladmin: ModelAdmin[Any], request: HttpRequestUser, queryset: QuerySet[Any]
) -> TemplateResponse | None: ...
