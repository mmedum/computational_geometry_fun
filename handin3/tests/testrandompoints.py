from unittest import TestCase

from experiments.generate import random_points_circle, random_points_square


class TestRandomPoints(TestCase):
    def test_random_points_circle(self):
        points = random_points_circle(100, 10)
        for point in points:
            if (point.x - 5) ** 2 + (point.y - 5) ** 2 > 25:
                self.fail()

    def test_random_points_square(self):
        points = random_points_square(100, 10, 10)
        for point in points:
            if point.x > 10 or point.y > 10:
                self.fail()
