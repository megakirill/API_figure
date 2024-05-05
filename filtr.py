from matplotlib.patches import Polygon
from matplotlib import path
from shapely.geometry import Polygon
from math import cos, sin, radians, sqrt


def flt_convex_polygon(polygon):
    def cross_product(p1, p2, p3):
        return (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])

    n = len(polygon)
    if n < 3:
        return False

    # Проверяем, что все вершины лежат на одной стороне от прямой, соединяющей первые две вершины
    sign = cross_product(polygon[0], polygon[1], polygon[2])
    for i in range(n):
        if cross_product(polygon[i], polygon[(i + 1) % n], polygon[(i + 2) % n]) * sign < 0:
            return False

    return True


def flt_angle_point(cords, polygon):
    return cords in polygon


def flt_square(s, figure):
    polygon = Polygon(figure)
    s1 = polygon.area
    print(s1)
    return s1 < s


def flt_short_side(l, figure):
    def len_shape(cord1, cord2):
        return sqrt(abs(cord1[0] - cord2[0]) ** 2 + abs(cord1[1] - cord2[1]) ** 2)

    for i in range(len(figure) - 1):
        if len_shape(figure[i], figure[i + 1]) < l:
            return False
    if len_shape(figure[-1], figure[0]) < l:
        return False
    return True


def flt_polygon_angles_inside(cords, polygon):
    return (cords in polygon) and flt_convex_polygon(polygon)


def flt_point_inside(cords, polygon):
    pa = path.Path(polygon)
    return not(pa.contains_point(cords))









