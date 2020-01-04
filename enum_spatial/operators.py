"""
Mixin with spatial operators
"""
from functools import lru_cache
from itertools import islice

import numpy as np
import pygeos
from pygeos.io import from_shapely


class SpatialOperators:

    @classmethod
    def _eval(cls, geoms, geom, operation):
        indices = np.where(getattr(pygeos, operation)(geoms, from_shapely(geom)))[0]
        if len(indices) == 0:
            raise AttributeError
        member_items = cls.__members__.items()
        values = [_[0] for _ in [next(islice(member_items, idx, idx+1)) for idx in indices]]
        return values[0] if len(values) == 1 else values

    @classmethod
    @lru_cache()
    def _shapely_to_pygeos(cls):
        return from_shapely([v for (k,v) in cls.__members__.items()])

    @classmethod
    def intersects(cls, geom):
        return cls._eval(cls._shapely_to_pygeos(), geom, "intersects")

    @classmethod
    def contains(cls, geom):
        return cls._eval(cls._shapely_to_pygeos(), geom, "contains")

    @classmethod
    def overlaps(cls, geom):
        return cls._eval(cls._shapely_to_pygeos(), geom, "overlaps")

    @classmethod
    def touches(cls, geom):
        return cls._eval(cls._shapely_to_pygeos(), geom, "touches")

    @classmethod
    def disjoint(cls, geom):
        return cls._eval(cls._shapely_to_pygeos(), geom, "disjoint")

    @classmethod
    def crosses(cls, geom):
        return cls._eval(cls._shapely_to_pygeos(), geom, "crosses")