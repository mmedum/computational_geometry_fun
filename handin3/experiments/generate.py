import random

from common.point import Point


def random_points_square(number=1000, max_x=100, max_y=100):
    points = []
    for i in range(1, number):
        x_cor = random.uniform(0, max_x)
        y_cor = random.uniform(0, max_y)
        points.append(Point(x_cor, y_cor))
    return points


def random_points_circle(number=1000, diameter=100):
    points = []
    radius = diameter / 2
    center_x = radius
    center_y = radius
    radius_squared = radius ** 2

    while len(points) < number:
        x_cor = random.uniform(0, diameter)
        y_cor = random.uniform(0, diameter)
        # Only add the coordinate if it's inside the periphery of the circle
        if (x_cor - center_x) ** 2 + (y_cor - center_y) ** 2 <= radius_squared:
            points.append(Point(x_cor, y_cor))

    return points


def random_points_curve(number=1000, max_x=100):
    points = []
    for i in range(1, number):
        x_cor = random.uniform(0, max_x)
        y_cor = x_cor ** 2
        points.append(Point(x_cor, y_cor))

    return points
