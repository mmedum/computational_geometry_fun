import time

import sys

from experiments.generate import random_points_square, random_points_circle, random_points_curve
from gift_wrapping import gift_wrap
from graham_scan import graham_scan
from marriage_before_conquest import marriage_before_conquest_v1
from quick_hull import quick_hull


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

    row = (str(i) for i in (number_of_points, avg_hull_size, avg_time))
    with open(algorithm.__name__ + "_" + generator.__name__ + ".csv", "a") as csv_file:
        csv_file.write(','.join(row))
        csv_file.write('\n')

    print("{} {} {}: average time: {} seconds"
          .format(algorithm.__name__, number_of_points, generator.__name__, avg_time))
    print("{} {} {}: average hull size: {} points"
          .format(algorithm.__name__, number_of_points, generator.__name__, avg_hull_size))


if __name__ == '__main__':
    numbers = []
    start = 10000
    upper_limit = int(sys.argv[1])

    # Generate doubling numbers up to the limit
    while start <= upper_limit:
        numbers.append(start)
        start *= 2
    # The point generator functions
    generators = [random_points_square, random_points_circle, random_points_curve]

    # The algorithms we want to run the experiments for
    algorithms = []
    for arg in sys.argv[2:]:
        if arg == "quick_hull":
            algorithms.append(quick_hull)
        elif arg == "gift_wrap":
            algorithms.append(gift_wrap)
        elif arg == "graham_scan":
            algorithms.append(graham_scan)
        elif arg == "marriage_before_conquest":
            algorithms.append(marriage_before_conquest_v1)

    # We run each algorithm in turn with each input class, increasing the number of points
    for algorithm in algorithms:
        for generator in generators:
            for number in numbers:
                experiment_run(generator, algorithm, number_of_points=number, repeats=5)
