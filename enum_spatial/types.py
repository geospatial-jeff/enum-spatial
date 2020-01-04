from enum import Enum

from shapely.geometry import (
    Point,
    LineString,
    Polygon,
    MultiPoint,
    MultiLineString,
    MultiPolygon,
)

from .operators import SpatialOperators


"""
Geometry specific enum types
"""
class PointEnum(SpatialOperators, Point, Enum):
    pass

class LineStringEnum(SpatialOperators, LineString, Enum):
    pass

class PolygonEnum(SpatialOperators, Polygon, Enum):
    pass

class MultiPointEnum(SpatialOperators, MultiPoint, Enum):
    pass

class MultiLineStringEnum(SpatialOperators, MultiLineString, Enum):
    pass

class MultiPolygonEnum(SpatialOperators, MultiPolygon, Enum):
    pass


"""
Other enum types
"""
class BoundsPoly(Polygon):

    def __init__(self, bounds):
        super().__init__(Polygon.from_bounds(*bounds))

class BoundsEnum(SpatialOperators, BoundsPoly, Enum):
    pass
