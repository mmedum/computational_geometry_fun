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
            points.append(Point(int(coordinates[0].strip()), int(coordinates[1].strip())))
    points.sort(key=lambda p: p.x)
    return points


# Three points are a counter-clockwise turn if ccw > 0, clockwise if
# ccw < 0, and collinear if ccw = 0 because ccw is a determinant that
# gives twice the signed  area of the triangle formed by p1, p2 and p3.
def ccw(p1, p2, p3):
    return (p2.x - p1.x)*(p3.y - p1.y) - (p2.y - p1.y)*(p3.x - p1.x)


def graham_scan(points):
    upper_hull = []
    for p in points:
        while len(upper_hull) > 1 and ccw(upper_hull[-2], upper_hull[-1], p) >= 0:
            upper_hull.pop()
        upper_hull.append(p)
    lower_hull = []
    for p in points:
        while len(lower_hull) > 1 and ccw(lower_hull[-2], lower_hull[-1], p) <= 0:
            lower_hull.pop()
        lower_hull.append(p)
    lower_hull.reverse()
    upper_hull.extend(lower_hull[1:])
    return upper_hull


def output_convex_hull(convex_hull):
    print('Graham Scan')
    for c in convex_hull:
        print(c)


if __name__ == '__main__':
    points = read_points('points')
    convex_hull = graham_scan(points)
    output_convex_hull(convex_hull)
