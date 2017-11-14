import numpy as np

from common import read_points, output_convex_hull, Point


def gift_wrap(points):
    convex_hull = []
    # Init: Find the point q_1 with min x coordinate, and initialize an upward ray r from q1, and set pivot p = q_1
    q_1 = Point(float('inf'), 0)
    for p in points:
        if p.x < q_1.x:
            q_1 = p
    pivot = q_1
    convex_hull.append(q_1)
    r = [0, 10]  # upward

    # Do until p is q_1 again
    while True:
        min_angle = 360
        u = None
        for point in points:
            if point == pivot:
                continue
            pu = [point.x - pivot.x, point.y - pivot.y]
            ang = angle(r, pu)
            if ang < min_angle:
                u = point
                min_angle = ang

        convex_hull.append(u)
        r = [u.x - pivot.x, u.y - pivot.y]
        pivot = u
        if pivot == q_1:
            break
    return convex_hull


def angle(v1, v2):
    """
    Returns the clockwise angle between the vectors.
    :param v1: array_like
    :param v2: array_like
    :return: angle in degrees
    """
    cos = np.dot(v1, v2)
    mag = np.linalg.norm(v1) * np.linalg.norm(v2)
    inner_angle = np.degrees(np.arccos(cos / mag))
    det = np.linalg.det([v1, v2])
    if det <= 0:
        return inner_angle
    else:
        return 360 - inner_angle


if __name__ == '__main__':
    points = read_points('points')
    convex_hull = gift_wrap(points)
    output_convex_hull('gift_wrap', convex_hull)
