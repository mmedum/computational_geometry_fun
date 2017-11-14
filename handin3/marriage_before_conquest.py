from common import read_points, output_convex_hull


def marriage_before_conquest_v1(points):
    # find the median (easy, since the points are already sorted)
    median_index = int(len(points) / 2)
    p_m = points[median_index]
    p_l = points[:median_index - 1]  # all points smaller than median
    p_r = points[median_index:]  # the rest

    return [p_m, p_l, p_r]
    # return points


if __name__ == '__main__':
    points = read_points('points')
    convex_hull = marriage_before_conquest_v1(points)
    output_convex_hull('gift_wrap', convex_hull)
