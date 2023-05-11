class Point:
    x: int
    y: int

    def __init__(self, x: int = 0, y: int = 0):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f'Point({self.x}, {self.y})'
    
    def __mul__(self, other):
        return Point(self.x * other, self.y * other)
    
    def __eq__(self, other):
        if type(other) != type(self):
            return False
        if self.x != other.x or self.y != other.y:
            return False
        return True

class Polygon:
    points: list[Point]

    def __init__(self, points: list[Point] = []):
        self.points = points

    def add_point(self, point: Point):
        self.points.append(point)

    def __str__(self):
        temp = 'Polygon['+ ' '.join(map(lambda x: str(x)+',', self.points))
        return temp[:len(temp)-1] + ']'
    
    def __getitem__(self, items) -> int | slice:
        try:
            return self.points[items]
        except TypeError: 
            print("This index does not exist")
            return self.points