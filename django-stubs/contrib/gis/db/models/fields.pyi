from collections.abc import Iterable
from typing import Any, NamedTuple, TypeVar

from django.contrib.gis import forms
from django.contrib.gis.geos import (
    GeometryCollection,
    GEOSGeometry,
    LineString,
    MultiLineString,
    MultiPoint,
    MultiPolygon,
    Point,
    Polygon,
)
from django.core.validators import _ValidatorCallable
from django.db.models import Model
from django.db.models.expressions import Combinable, Expression
from django.db.models.fields import NOT_PROVIDED, Field, _ErrorMessagesMapping
from django.utils.choices import _Choices
from django.utils.functional import _StrOrPromise

# __set__ value type
_ST = TypeVar("_ST", contravariant=True, default=Any)
# __get__ return type
_GT = TypeVar("_GT", covariant=True, default=Any)
# null type
_NT = TypeVar("_NT", Literal[True], Literal[False], default=Literal[False])

class SRIDCacheEntry(NamedTuple):
    units: Any
    units_name: str
    spheroid: str
    geodetic: bool

def get_srid_info(srid: int, connection: Any) -> SRIDCacheEntry: ...

class BaseSpatialField(Field[_ST, _GT, _NT]):
    form_class: type[forms.GeometryField]
    geom_type: str
    geom_class: type[GEOSGeometry] | None
    geography: bool
    spatial_index: bool
    srid: int
    def __init__(
        self,
        verbose_name: _StrOrPromise | None = ...,
        srid: int = ...,
        spatial_index: bool = ...,
        *,
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
    def db_type(self, connection: Any) -> Any: ...
    def spheroid(self, connection: Any) -> Any: ...
    def units(self, connection: Any) -> Any: ...
    def units_name(self, connection: Any) -> Any: ...
    def geodetic(self, connection: Any) -> Any: ...
    def get_placeholder(self, value: Any, compiler: Any, connection: Any) -> Any: ...
    def get_srid(self, obj: Any) -> Any: ...
    def get_db_prep_value(self, value: Any, connection: Any, *args: Any, **kwargs: Any) -> Any: ...
    def get_raster_prep_value(self, value: Any, is_candidate: Any) -> Any: ...
    def get_prep_value(self, value: Any) -> Any: ...

class GeometryField(BaseSpatialField[_ST, _GT, _NT]):
    dim: int
    def __init__(
        self,
        verbose_name: _StrOrPromise | None = ...,
        dim: int = ...,
        geography: bool = ...,
        *,
        extent: tuple[float, float, float, float] = ...,
        tolerance: float = ...,
        srid: int = ...,
        spatial_index: bool = ...,
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
    def formfield(  # type: ignore[override]
        self,
        *,
        form_class: type[forms.GeometryField] | None = ...,
        geom_type: str = ...,
        srid: Any = ...,
        **kwargs: Any,
    ) -> forms.GeometryField: ...
    def contribute_to_class(self, cls: type[Model], name: str, **kwargs: Any) -> None: ...  # type: ignore[override]

_ST_PointField = TypeVar("_ST_PointField", bound=Point | Combinable, default=Point | Combinable)
_GT_PointField = TypeVar("_GT_PointField", bound=Point, default=Point)

class PointField(GeometryField[_ST_PointField, _GT_PointField, _NT]):
    _pyi_private_set_type: Point | Combinable
    _pyi_private_get_type: Point
    _pyi_lookup_exact_type: Point

    geom_class: type[Point]
    form_class: type[forms.PointField]

_ST_LineStringField = TypeVar("_ST_LineStringField", bound=LineString | Combinable, default=LineString | Combinable)
_GT_LineStringField = TypeVar("_GT_LineStringField", bound=LineString, default=LineString)

class LineStringField(GeometryField[_ST_LineStringField, _GT_LineStringField, _NT]):
    _pyi_private_set_type: LineString | Combinable
    _pyi_private_get_type: LineString
    _pyi_lookup_exact_type: LineString

    geom_class: type[LineString]
    form_class: type[forms.LineStringField]

_ST_PolygonField = TypeVar("_ST_PolygonField", bound=Polygon | Combinable, default=Polygon | Combinable)
_GT_PolygonField = TypeVar("_GT_PolygonField", bound=Polygon, default=Polygon)

class PolygonField(GeometryField[_ST_PolygonField, _GT_PolygonField, _NT]):
    _pyi_private_set_type: Polygon | Combinable
    _pyi_private_get_type: Polygon
    _pyi_lookup_exact_type: Polygon

    geom_class: type[Polygon]
    form_class: type[forms.PolygonField]

_ST_MultiPointField = TypeVar("_ST_MultiPointField", bound=MultiPoint | Combinable, default=MultiPoint | Combinable)
_GT_MultiPointField = TypeVar("_GT_MultiPointField", bound=MultiPoint, default=MultiPoint)

class MultiPointField(GeometryField[_ST_MultiPointField, _GT_MultiPointField, _NT]):
    _pyi_private_set_type: MultiPoint | Combinable
    _pyi_private_get_type: MultiPoint
    _pyi_lookup_exact_type: MultiPoint

    geom_class: type[MultiPoint]
    form_class: type[forms.MultiPointField]

_ST_MultiLineStringField = TypeVar("_ST_MultiLineStringField", bound=MultiLineString | Combinable, default=MultiLineString | Combinable)
_GT_MultiLineStringField = TypeVar("_GT_MultiLineStringField", bound=MultiLineString, default=MultiLineString)

class MultiLineStringField(GeometryField[_ST_MultiLineStringField, _GT_MultiLineStringField, _NT]):
    _pyi_private_set_type: MultiLineString | Combinable
    _pyi_private_get_type: MultiLineString
    _pyi_lookup_exact_type: MultiLineString

    geom_class: type[MultiLineString]
    form_class: type[forms.MultiLineStringField]

_ST_MultiPolygonField = TypeVar("_ST_MultiPolygonField", bound=MultiPolygon | Combinable, default=MultiPolygon | Combinable)
_GT_MultiPolygonField = TypeVar("_GT_MultiPolygonField", bound=MultiPolygon, default=MultiPolygon)

class MultiPolygonField(GeometryField[_ST_MultiPolygonField, _GT_MultiPolygonField, _NT]):
    _pyi_private_set_type: MultiPolygon | Combinable
    _pyi_private_get_type: MultiPolygon
    _pyi_lookup_exact_type: MultiPolygon

    geom_class: type[MultiPolygon]
    form_class: type[forms.MultiPolygonField]

_ST_GeometryCollectionField = TypeVar("_ST_GeometryCollectionField", bound=GeometryCollection | Combinable, default=GeometryCollection | Combinable)
_GT_GeometryCollectionField = TypeVar("_GT_GeometryCollectionField", bound=GeometryCollection, default=GeometryCollection)

class GeometryCollectionField(GeometryField[_ST_GeometryCollectionField, _GT_GeometryCollectionField, _NT]):
    _pyi_private_set_type: GeometryCollection | Combinable
    _pyi_private_get_type: GeometryCollection
    _pyi_lookup_exact_type: GeometryCollection

    geom_class: type[GeometryCollection]
    form_class: type[forms.GeometryCollectionField]

class ExtentField(Field):
    def get_internal_type(self) -> Any: ...

class RasterField(BaseSpatialField):
    def db_type(self, connection: Any) -> Any: ...
    def from_db_value(self, value: Any, expression: Any, connection: Any) -> Any: ...
    def contribute_to_class(self, cls: type[Model], name: str, **kwargs: Any) -> None: ...  # type: ignore[override]
    def get_transform(self, name: Any) -> Any: ...
