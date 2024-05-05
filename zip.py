from itertools import chain
from main import *


def zip_polygons(*iterators):
    result = []
    max_length = max(len(iterator) for iterator in iterators)
    for i in range(max_length):
        new_polygon = []
        t = True
        for iterator in iterators:
            if i < len(iterator):
                new_polygon.extend(iterator[i])
        result.append(new_polygon)

    return result
a = zip_polygons([((1, 1), (2, 2), (3, 1)), ((11, 11), (12, 12), (13, 11))], [((1, -1), (2, -2), (3, -1)), ((11, -11), (12, -12), (13, -11))])
visual_inf(a)

def count_2D(start, step):
    x, y = start
    while True:
        yield (x + step[0], y + step[1])
        x += step[0]
        y += step[1]
a = count_2D((0, 0), (1, 1))


def zip_tuple(*iterators):
    result = []
    min_length = min(len(iterator) for iterator in iterators)
    for i in range(min_length):
        new_polygon = []
        for iterator in iterators:
            new_polygon.append(iterator[i])
        result.append(new_polygon)
    return result
