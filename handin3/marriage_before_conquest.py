from common import read_points, output_convex_hull, linprog
import random


def marriage_before_conquest_v1(points):
    # Step 1
    upper_hull = []
    sample_elements = random.sample(points, 3)
    sample_elements.sort(key=lambda p: p.x)
    median_element = sample_elements[2]
    print('Median element {}'.format(median_element))

    points_left = []
    points_right = []
    for p in points:
        if p.x < median_element.x:
            points_left.append(p)
        else:
            points_right.append(p)

    linprog.lin_prog_2d(points, median_element)

    upper_hull.extend(marriage_before_conquest_v1(points_left))
    upper_hull.extend(marriage_before_conquest_v1(points_right))
    print(upper_hull)

    return upper_hull


if __name__ == '__main__':
    points = read_points('points')
    convex_hull = marriage_before_conquest_v1(points)
    output_convex_hull('gift_wrap', convex_hull)
