We maintain our own fork of `django-stubs`, since `django-types` has some problems and is slow to update 

## Setup

You must create a `django_types.pyi` file in the project root to define project specific types for `User` and `HttpRequest`. For example:

```python
from django.http.request import BaseHttpRequest

from accounts.models import Account
from htmx.middleware import HtmxDetails

User = Account

class HttpRequest(BaseHttpRequest):
    htmx: HtmxDetails
```

## Fields

We replace the mypy plugin with default generics and overloads. This is similar to how `django-types` does it, but with much less code because of the `_NT` generic.

```python
_ST = TypeVar("_ST", contravariant=True, default=Any)
_GT = TypeVar("_GT", covariant=True, default=Any)
_NT = TypeVar("_NT", Literal[True], Literal[False], default=Literal[False])

class Field(..., Generic[_ST, _GT, _NT]):
    ...
    def __init__(self, ..., null: _NT = False, ...) -> None: ...
    @overload
    def __set__(self: Field[Any, Any, Literal[False]], instance: Any, value: _ST) -> None: ...
    @overload
    def __set__(self: Field[Any, Any, Literal[True]], instance: Any, value: _ST | None) -> None: ...
    # class access
    @overload
    def __get__(self, instance: None, owner: Any) -> _FieldDescriptor[Self]: ...
    # Model instance access
    @overload
    def __get__(self: Field[Any, Any, Literal[False]], instance: Model, owner: Any) -> _GT: ...
    @overload
    def __get__(self: Field[Any, Any, Literal[True]], instance: Model, owner: Any) -> _GT | None: ...
    # non-Model instances
    @overload
    def __get__(self, instance: Any, owner: Any) -> Self: ...
    ...
```

Then we further bound specific fields as follows:

```python
_ST_IntegerField = TypeVar("_ST_IntegerField", bound=float | int | str | Combinable, default=float | int | str | Combinable)
_GT_IntegerField = TypeVar("_GT_IntegerField", bound=int, default=int)

class IntegerField(Field[_ST_IntegerField, _GT_IntegerField, _NT]):
    ....
```

## Managers

Also we add a queryset generic to managers. `django-types` assume the model `Manager` and `QuerySet` are the same, but this is never true.

```python
_T = TypeVar("_T", bound=Model, covariant=True)
_QS = TypeVar("_QS", bound=QuerySet[Any], contravariant=True, default=QuerySet[_T, _T])

class BaseManager(Generic[_T, _QS]):
    ...
    def get_queryset(self) -> _QS: ...
    def all(self) -> _QS: ...
```

Then you define custom manager and querysets as follows

```python
class CustomQuerySet(QuerySet["CustomModel"]):
    def custom_method_1(self, ...):
        ...

    def custom_method_2(self, ...):
        ...

class CustomManager(Manager["CustomModel", CustomQuerySet]):
    _queryset_class = AllowListQuerySet

    def get_queryset(self):
        return CustomQuerySet(self.model, using=self._db)

    def custom_method_1(self, ...):
        return self.get_queryset().custom_method_1(...)

    def custom_method_2(self, ...):
        return self.get_queryset().custom_method_2(...)
```

The boilerplate code in `CustomManager` is required because `.as_manager()` and `.from_queryset()` are not type safe

## Forms

Finally we add a `_Cleaned` generic to `BaseForm` for a bit more type safety in form.

```python
_Cleaned = TypeVar("_Cleaned", bound=Mapping[str, Any], default=dict[str, Any])

class BaseForm(..., Generic[_Cleaned]):
    ...
    cleaned_data: _Cleaned
    ....
    def clean(self) -> _Cleaned | None: ...
    ...
```

## Related Manager

Note the `RelatedManager` is now imported differently 

```python
if TYPE_CHECKING:
    from django.db.models.fields.related_descriptors import RelatedManager
```

## Authentication

We add a new `HttpRequestUser` class for when we know the request is authenticated.

```python
class HttpRequestUser(HttpRequest):
    user: _User
```