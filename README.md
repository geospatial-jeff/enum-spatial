# spatial-enum
Enumerations for spatial data with support for vectorized spatial operations via [`pygeos`](https://github.com/pygeos/pygeos).

```python
from enum_spatial import BoundsEnum
from shapely.geometry import Point

class MyEnum(BoundsEnum):
    bbox1 = [-118, 34, -117, 35]
    bbox2 = [-81, 30, -80, 31]

print(MyEnum.bbox1)
>>> POLYGON ((-118 34, -118 35, -117 35, -117 34, -118 34))

print(MyEnum.intersects(Point([-117.5, 34.5]))
>>> bbox1
```

Supported enum types:
- `BoundsEnum`
- `PointEnum`
- `LineStringEnum`
- `PolygonEnum`
- `MultiPointEnum`
- `MultiLineStringEnum`
- `MultiPolygonEnum`

Support spatial operations:
- `intersects`
- `contains`
- `overlaps`
- `touches`
- `disjoint`
- `crosses`

## Installation
```python
pip install shapely --no-binary shapely
pip install git+https://github.com/geospatial-jeff/enum-spatial.git
```

### World Cities Example
Download the dataset:
```bash
curl https://raw.githubusercontent.com/datasets/geo-countries/master/data/countries.geojson -o countries.geojson
```

Load into the enum through the `enum.Enum` [functional API](https://docs.python.org/3/library/enum.html#functional-api):
```python
import json
from enum_spatial import MultiPolygonEnum
from shapely.geometry import shape

data = json.load(open('countries.geojson', 'r'))
enum_members = []
for feat in data['features']:
    geom = shape(feat['geometry'])
    country_name = feat['properties']['ADMIN']
    if geom.is_valid:
        enum_members.append((country_name, geom))

world_countries = MultiPolygonEnum('WorldCountries', enum_members)
```

Find a country which contains a given point:
```python
print(world_countries.intersects(Point([-54, 15])))
>>> Brazil
```

Find neighboring countries:
```python
print(world_countries.intersects(world_countries.Paraguay))
>>> ['Argentina', 'Bolivia', 'Brazil', 'Paraguay']
```