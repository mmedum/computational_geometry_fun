from common import point
import random


def linear_prog_1d(constraints, obj_function):
    right = float('inf')
    left = float('-inf')

    for constraint in constraints:
        if constraint.x == 0:
            if constraint.y > 0:
                return None
        else:
            ratio = constraint.y / constraint.x
            if constraint.x > 0:
                left = max(left, ratio)
            else:
                right = min(right, ratio)

    if left > right:
        return None

    if obj_function >= 0:
        return left
    else:
        return right


def calculate_a_and_b(p, q):
    a = (q.y - p.y) / (q.x - p.x)
    b = p.y - a * p.x
    return a, b


def satisfy(a, b, constraint):
    return constraint.y <= a * constraint.x + b


def linear_prog(points_left, points_right, median):
    left = points_left[0]
    right = points_right[0]

    if len(points_left) == 1 and len(points_right) == 1:
        return left, right

    a, b = calculate_a_and_b(left, right)

    constraints = []
    constraints.append(left)
    constraints.append(right)
    points = points_left[1:]
    points.extend(points_right[1:])
    for p in points:
        if not satisfy(a, b, p):
            constraints_in_1d = []
            for c in constraints:
                constraints_in_1d.append(point.Point(c.x - p.x, c.y - p.y))
            obj_function = median.x - p.x
            a = linear_prog_1d(constraints_in_1d, obj_function)
            b = p.y - a * p.x
        constraints.append(p)
    return a, b


def find_min_point(a, b, points):
    min_dis = float('inf')
    min_point = points[0]
    for p in points:
        dis = (a * p.x + b) - p.y
        if dis < min_dis:
            min_point = p
            min_dis = dis
    return min_point


def prune_left(line_segment, points):
    survived_points = []
    for p in points:
        if p.x < line_segment[0].x:
            survived_points.append(p)
    return survived_points


def prune_right(line_segment, points):
    survived_points = []
    for p in points:
        if p.x > line_segment[1].x:
            survived_points.append(p)
    return survived_points


def marriage_before_conquest_v1(points):
    hull = []
    if len(points) <= 1:
        return hull

    if len(points) == 2:
        line_segment = [points[0], points[1]]
        hull.append(line_segment)
        return hull

    sample_elements = random.sample(points, 3)
    sample_elements.sort(key=lambda p: p.x)
    median = sample_elements[1]

    points_left = []
    points_right = []
    for p in points:
        if p is median:
            points_left.append(p)
        elif p.x < median.x:
            points_left.append(p)
        else:
            points_right.append(p)

    random.shuffle(points_left)
    random.shuffle(points_right)
    a, b = linear_prog(points_left, points_right, median)

    min_left_point = find_min_point(a, b, points_left)
    min_right_point = find_min_point(a, b, points_right)
    line_segment = [min_left_point, min_right_point]

    points_left = prune_left(line_segment, points_left)
    points_left.append(min_left_point)

    points_right = prune_right(line_segment, points_right)
    points_right.append(min_right_point)

    hull.extend(marriage_before_conquest_v1(points_left))
    hull.append(line_segment)
    hull.extend(marriage_before_conquest_v1(points_right))

    return hull


if __name__ == '__main__':
    points = point.read_points('points')
    convex_hull = marriage_before_conquest_v1(points)
    print(convex_hull)
