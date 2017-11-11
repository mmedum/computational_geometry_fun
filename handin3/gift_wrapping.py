import numpy as np

from common import read_points, output_convex_hull


def gift_wrap(points):
    convex_hull = []
    # Init: Find the point q_1 with min x coordinate, and initialize an upward ray r from q1, and set pivot p = q_1
    q_1 = points[0]  # points are already sorted
    p = q_1
    convex_hull.append(q_1)
    r = [0, 100]  # upward
    print("q_1", q_1)

    # Do until p is q_1 again
    for i in range(0, 10):
        min_angle = 360
        u = None
        for point in points:
            if point == p:
                continue
            pu = [point.x - p.x, point.y - p.y]
            ang = angle(r, pu)
            if ang < min_angle:
                u = point
                min_angle = ang

        convex_hull.append(u)
        p = u
        print(u, min_angle)
        if p == q_1:
            print("I should stop")
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
    upper_hull = gift_wrap(points)
    output_convex_hull('gift_wrap', upper_hull)
