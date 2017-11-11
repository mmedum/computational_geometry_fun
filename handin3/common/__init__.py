class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    def __str__(self):
        return '{},{}'.format(self._x, self._y)


def read_points(path):
    points = []
    with open(path, 'r') as file:
        for line in file.readlines():
            coordinates = line.split(',')
            points.append(Point(float(coordinates[0].strip()), float(coordinates[1].strip())))
    points.sort(key=lambda p: p.x)
    return points


# Three points are a counter-clockwise turn if ccw > 0, clockwise if
# ccw < 0, and collinear if ccw = 0 because ccw is a determinant that
# gives twice the signed  area of the triangle formed by p1, p2 and p3.
def ccw(p1, p2, p3):
    return (p2.x - p1.x) * (p3.y - p1.y) - (p2.y - p1.y) * (p3.x - p1.x)


def output_convex_hull(title, convex_hull):
    print(title)
    for c in convex_hull:
        print(c)
