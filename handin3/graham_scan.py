# Three points are a counter-clockwise turn if ccw > 0, clockwise if
# ccw < 0, and collinear if ccw = 0 because ccw is a determinant that
# gives twice the signed  area of the triangle formed by p1, p2 and p3.
from common import read_points, ccw


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
