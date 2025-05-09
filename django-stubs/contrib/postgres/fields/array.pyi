from collections.abc import Iterable, Sequence
from typing import Any, ClassVar, Literal, TypeVar

from _typeshed import Unused
from django.core.validators import _ValidatorCallable
from django.db.backends.base.base import BaseDatabaseWrapper
from django.db.models import Field
from django.db.models.expressions import Combinable, Expression
from django.db.models.fields import NOT_PROVIDED, _ErrorMessagesDict, _ErrorMessagesMapping
from django.db.models.fields.mixins import CheckFieldDefaultMixin
from django.db.models.lookups import Transform
from django.utils.choices import _Choices
from django.utils.functional import _StrOrPromise

_ST_ArrayField = TypeVar("_ST_ArrayField", bound=Sequence[Any] | Combinable, default=Sequence[Any] | Combinable)
_GT_ArrayField = TypeVar("_GT_ArrayField", bound=list[Any], default=list[Any])
_NT = TypeVar("_NT", Literal[True], Literal[False], default=Literal[False])

class ArrayField(CheckFieldDefaultMixin, Field[_ST_ArrayField, _GT_ArrayField, _NT]):
    _pyi_private_set_type: Sequence[Any] | Combinable
    _pyi_private_get_type: list[Any]

    empty_strings_allowed: bool
    default_error_messages: ClassVar[_ErrorMessagesDict]
    base_field: Field
    size: int | None
    default_validators: Sequence[_ValidatorCallable]
    from_db_value: Any
    def __init__(
        self,
        base_field: Field,
        size: int | None = None,
        *,
        verbose_name: _StrOrPromise | None = ...,
        name: str | None = ...,
        primary_key: bool = ...,
        max_length: int | None = ...,
        unique: bool = ...,
        blank: bool = ...,
        null: _NT = ...,
        db_index: bool = ...,
        default: Any = ...,
        db_default: type[NOT_PROVIDED] | Expression | _ST = ...,
        editable: bool = ...,
        auto_created: bool = ...,
        serialize: bool = ...,
        unique_for_date: str | None = ...,
        unique_for_month: str | None = ...,
        unique_for_year: str | None = ...,
        choices: _Choices | None = ...,
        help_text: _StrOrPromise = ...,
        db_column: str | None = ...,
        db_comment: str | None = ...,
        db_tablespace: str | None = ...,
        validators: Iterable[_ValidatorCallable] = ...,
        error_messages: _ErrorMessagesMapping | None = ...,
    ) -> None: ...
    @property
    def description(self) -> str: ...  # type: ignore[override]
    def cast_db_type(self, connection: BaseDatabaseWrapper) -> str: ...
    def get_placeholder(self, value: Unused, compiler: Unused, connection: BaseDatabaseWrapper) -> str: ...
    def get_transform(self, name: str) -> type[Transform] | None: ...

__all__ = ["ArrayField"]
