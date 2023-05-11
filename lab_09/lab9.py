from utils import Point, Polygon

punkt1 = Point(2,4)
print(punkt1)
# print(2 * punkt1) # nie działa
print(punkt1 * 2)

print(punkt1 == 4)
print(punkt1 == Point(2,4))
print(punkt1 == {'x': 2, 'y': 4})


poligon = Polygon([punkt1])

poligon.add_point(Point(12,16))

print(poligon)