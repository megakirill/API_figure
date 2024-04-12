from itertools import chain
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from functools import reduce
from math import cos, sin, radians


def generate_pol(pol_specs):
    return map(lambda spec: Polygon(spec), pol_specs)  # niggers_sucks


def transform_pol(polygon_sequence, transformations):
    return map(lambda polygon: reduce(lambda p, t: t(p), transformations, polygon), polygon_sequence)


def visual(polygon_sequence):
    fig, ax = plt.subplots()
    for polygon in polygon_sequence:
        ax.add_patch(polygon)
    ax.autoscale()
    plt.axis('equal')
    plt.show()


def gen_rectangle(start_point, width, height, spacing):
    x, y = start_point
    while True:
        yield [(x, y), (x + width, y), (x + width, y + height), (x, y + height)]
        x += width + spacing


def gen_triangle(start_point, side_length, spacing):
    x, y = start_point
    while True:
        yield [(x, y), (x + side_length, y), (x + side_length / 2, y + (3 ** 0.5 / 2) * side_length)]
        x += side_length + spacing


def gen_hexagon(start_point, side_length, spacing):
    x, y = start_point
    while True:
        yield [(x + side_length * (3 ** 0.5) / 2, y - side_length / 2),
               (x + side_length * (3 ** 0.5), y),
               (x + side_length * (3 ** 0.5) / 2, y + side_length / 2),
               (x - side_length * (3 ** 0.5) / 2, y + side_length / 2),
               (x - side_length * (3 ** 0.5), y),
               (x - side_length * (3 ** 0.5) / 2, y - side_length / 2)]
        x += 2 * side_length * (3 ** 0.5) + spacing


def visual_inf(sequence, num_figures=7):
    fig, ax = plt.subplots()
    for _ in range(num_figures):
        polygon = next(sequence)
        ax.add_patch(Polygon(polygon, closed=True))
    ax.autoscale()
    plt.axis('equal')
    plt.show()


def tr_translate(args):
    polygon, dx, dy = args
    return [(x + dx, y + dy) for x, y in polygon]


def tr_rotate(args):
    polygon, angle, origin = args
    ox, oy = origin
    angle_rad = radians(angle)
    return [(cos(angle_rad) * (x - ox) - sin(angle_rad) * (y - oy) + ox,
             sin(angle_rad) * (x - ox) + cos(angle_rad) * (y - oy) + oy) for x, y in polygon]


def tr_symmetry(args):
    polygon, axis = args
    if axis == 'x':
        return [(x, -y) for x, y in polygon]
    elif axis == 'y':
        return [(-x, y) for x, y in polygon]


def tr_homothety(args):
    polygon, factor, origin = args
    ox, oy = origin
    return [(ox + (x - ox) * factor, oy + (y - oy) * factor) for x, y in polygon]


if __name__ == "__main__":
    pol_specs = [((0, 0), (0, 1), (1, 1), (1, 0)), ((0, 0), (0, 2), (2, 2), (2, 0))]

    polygons = generate_pol(pol_specs)

    transformations = [lambda p: (p[0] + 1, p[1] + 1)]
    transformed_pol = transform_pol(polygons, transformations)

    visual(chain(polygons, transformed_pol))

    rectangle_sequence = gen_rectangle((0, 0), 2, 1, 0.5)
    visual_inf(rectangle_sequence)

    triangle_sequence = gen_triangle((0, 0), 2, 0.5)
    visual_inf(triangle_sequence)

    hexagon_sequence = gen_hexagon((0, 0), 1, 0.5)
    visual_inf(hexagon_sequence)
