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


def output_convex_hull(title, quick_hull):
    print(title)
    for c in quick_hull:
        print('({}, {})'.format(c[0], c[1]))


# Three points are a counter-clockwise turn if ccw > 0, clockwise if
# ccw < 0, and collinear if ccw = 0 because ccw is a determinant that
# gives twice the signed  area of the triangle formed by p1, p2 and p3.
def sidedness_test(p1, p2, p3):
    return (p2.x - p1.x)*(p3.y - p1.y) - (p2.y - p1.y)*(p3.x - p1.x)


def distance_point_to_line(p1, p2, p3):
    return abs((p2.x - p1.x)*(p3.y - p1.y) - (p2.y - p1.y)*(p3.x - p1.x))


def prune(line_segment, points):
    pruned_points = []
    for p in points:
        if sidedness_test(line_segment[0], line_segment[1], p) >= 0:
            pruned_points.append(p)
    return pruned_points


def find_point_with_largest_distance(line_segment, points):
    max_distance = -1
    max_point = None
    for p in points:
        current_distance = distance_point_to_line(line_segment[0], line_segment[1], p)
        if current_distance > max_distance:
            max_distance = current_distance
            max_point = p
    return max_point


def rec_quick_hull(line_segment, points):
    if len(points) == 0 or points is None:
        return [(line_segment[0], line_segment[1])]
    largest_distance_point = find_point_with_largest_distance(line_segment, points)
    upper_hull = []

    left_points = []
    right_points = []
    for p in points:
        if p.x <= largest_distance_point.x:
            if p.x != largest_distance_point.x or p.y != largest_distance_point.y:
                left_points.append(p)
        else:
            right_points.append(p)

    left_line_segment = (line_segment[0], largest_distance_point)
    left_pruned_points = prune(left_line_segment, left_points)

    right_line_segment = (largest_distance_point, line_segment[1])
    right_pruned_points = prune(right_line_segment, right_points)

    upper_hull.extend(rec_quick_hull(left_line_segment, left_pruned_points))
    upper_hull.extend(rec_quick_hull(right_line_segment, right_pruned_points))
    return upper_hull


def quick_hull(points):
    points.sort(key=lambda p: p.x)
    smallest = points[0]
    largest = points[-1]
    line_segment = (smallest, largest)
    pruned_points = prune(line_segment, points[1:-2])
    return rec_quick_hull(line_segment, pruned_points)


if __name__ == '__main__':
    points = read_points('points')
    upper_hull = quick_hull(points)
    output_convex_hull('quick_hull', upper_hull)
