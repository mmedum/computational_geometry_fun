from common.point import ccw, read_points, output_convex_hull


def graham_scan(points):
    points.sort(key=lambda p: p.x)
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


if __name__ == '__main__':
    points = read_points('points')
    convex_hull = graham_scan(points)
    output_convex_hull('graham scan', convex_hull)
