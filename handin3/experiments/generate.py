import random

from math import sqrt

from common.point import Point


def random_points_square(number=1000, max_x=None, max_y=None):
    if max_x is None:
        max_x = number / 10
    if max_y is None:
        max_y = number / 10

    points = []
    for i in range(1, number):
        x_cor = random.uniform(0, max_x)
        y_cor = random.uniform(0, max_y)
        points.append(Point(x_cor, y_cor))
    return points


def random_points_circle(number=1000, diameter=None):
    if diameter is None:
        diameter = number / 10

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


def random_points_curve(number=1000, max_x=None):
    if max_x is None:
        max_x = number / 10

    points = []
    for i in range(1, number):
        x_cor = random.uniform(0, max_x)
        y_cor = sqrt(x_cor)
        points.append(Point(x_cor, y_cor))
    return points
