import time

from experiments.generate import random_points_square, random_points_circle, random_points_curve
from graham_scan import graham_scan


def experiment_run(points_generator, algorithm, number_of_points=10000, repeats=3):
    timings = []
    size_of_hull = []
    for repeat in range(0, repeats):
        circle_points = points_generator(number=number_of_points)
        time_before = time.time()
        convex_hull = algorithm(circle_points)
        time_after = time.time()
        timing = time_after - time_before
        timings.append(timing)
        size_of_hull.append(len(convex_hull))
    avg_time = sum(timings) / len(timings)
    avg_hull_size = sum(size_of_hull) / len(size_of_hull)
    print("{}: average time: {} seconds".format(generator.__name__, avg_time))
    print("{}: average hull size: {} points".format(generator.__name__, avg_hull_size))


if __name__ == '__main__':
    number = 1000000
    generators = [random_points_square, random_points_circle, random_points_curve]
    algos = [graham_scan]

    for algo in algos:
        for generator in generators:
            experiment_run(generator, algo, number_of_points=number, repeats=1)
