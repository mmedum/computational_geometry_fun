from common import read_points, ccw, output_convex_hull


def distance_point_to_line(p1, p2, p3):
    return abs((p2.x - p1.x)*(p3.y - p1.y) - (p2.y - p1.y)*(p3.x - p1.x))


def prune(line_segment, points):
    pruned_points = []
    for p in points:
        if ccw(line_segment[0], line_segment[1], p) >= 0:
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
    smallest = points[0]
    largest = points[-1]
    line_segment = (smallest, largest)
    pruned_points = prune(line_segment, points[1:-2])
    return rec_quick_hull(line_segment, pruned_points)


if __name__ == '__main__':
    points = read_points('points')
    upper_hull = quick_hull(points)
    output_convex_hull('quick_hull', upper_hull)
