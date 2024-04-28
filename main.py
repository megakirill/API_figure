from itertools import chain  # объединение последовательностей в одну последовательность
import matplotlib.pyplot as plt  # используется для создания графиков и визуализации данных
from matplotlib.patches import Polygon  # используется для представления и отображения многоугольников
from functools import reduce
import math
import numpy as np


def generate_pol(pol_list):
    return map(lambda x: Polygon(x), pol_list)


def visual(pol_order):
    fig, ax = plt.subplots()
    for polygon in pol_order:
        ax.add_patch(polygon)
    ax.autoscale()
    plt.axis('equal')
    plt.show()


def gen_rectangle(start, width, height, spacex, spacey):
    x, y = start
    while True:
        yield [(x, y),
               (x + width, y), (x + width, y + height),
               (x, y + height)]

        x += spacex
        y += spacey


def gen_triangle(start, side_length, spacex, spacey):
    x, y = start
    while True:
        yield [(x, y),
               (x + side_length, y),
               (x + side_length / 2, y + math.sqrt(side_length ** 2 + (side_length / 2) ** 2))]

        x += spacex
        y += spacey


def gen_six(start, side_length, spacex, spacey):
    x, y = start
    while True:
        yield [(x, y),
               (x + side_length, y),
               (x + side_length * 3 / 2, y + (math.sqrt(3) / 2) * side_length),
               (x + side_length, y + math.sqrt(3) * side_length),
               (x, y + math.sqrt(3) * side_length),
               (x - side_length / 2, y + (math.sqrt(3) / 2) * side_length)]

        x += spacex
        y += spacey


def generate_figure(order, n):
    if n == 1:
        polygon = next(order)
    else:
        polygon = []
        for i in range(n):
            polygon.append(next(order))
    return polygon


def visual_inf(*cord):
    fig, ax = plt.subplots()
    for i in cord:
        for j in i:
            print(j)
            ax.add_patch(Polygon(j, closed=True))
    ax.autoscale()
    plt.axis('equal')
    plt.show()


def tr_translate(cords, distance=10):  # Параллель относительно x
    cords = cords[0], cords[1] + distance
    return cords


def tr_homothety(cords):
    return -cords[0], -cords[1]


def tr_symmetry(cords, axis='x'):
    # Преобразование списка вершин в массив numpy
    vertices = np.array(cords)

    # Создание матрицы отражения
    if axis == 'x':
        matrix = np.array([[1, 0], [0, -1]])
    else:
        np.array([[-1, 0], [0, 1]])

    # Отражение вершин
    polygon = np.dot(vertices, matrix)

    # Возврат списка вершин после создания симметрии
    return polygon.tolist()


def tr_rotate(polygon, angle=45):
    # Преобразование списка вершин в массив numpy
    vertices = np.array(polygon)

    # Создание матрицы поворота
    rotation_matrix = np.array([[np.cos(np.radians(angle)), -np.sin(np.radians(angle))],
                                [np.sin(np.radians(angle)), np.cos(np.radians(angle))]])

    # Поворот вершин
    rotated_vertices = np.dot(vertices, rotation_matrix)

    # Возврат списка вершин после поворота
    return rotated_vertices.tolist()


a = generate_figure(gen_rectangle((0, 0), 5, 2, 7, 0), 7)

b = [list(map(lambda polygon: tr_translate(polygon, 5), i)) for i in a]
c = [list(map(lambda polygon: tr_translate(polygon, 5), i)) for i in b]
a = [list(map(lambda polygon: tr_rotate(polygon, -45), i)) for i in a]
b = [list(map(lambda polygon: tr_rotate(polygon, -45), i)) for i in b]
c = [list(map(lambda polygon: tr_rotate(polygon, -45), i)) for i in c]
visual_inf(a, b, c)

a = generate_figure(gen_rectangle((-20, 0), 5, 2, 7, 0), 7)
b = generate_figure(gen_rectangle((25, 0), 5, 2, -7, 0), 7)
c = [list(map(lambda polygon: tr_rotate(polygon, -45), i)) for i in a]
b = [list(map(lambda polygon: tr_rotate(polygon, 45), i)) for i in b]
visual_inf(b, c)

a = generate_figure(gen_triangle((0, -7), 5, 7, 0), 7)
b = [list(map(lambda polygon: tr_symmetry(polygon, 'x'), i)) for i in a]
visual_inf(a, b)