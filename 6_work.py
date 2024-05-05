from main import *
from filtr import *

a = generate_figure(gen_rectangle((0, 0), 0.75, 5, 0.5, -0.5), 5)
c = [list(map(lambda polygon: tr_rotate(polygon, -45), i)) for i in a]
b = [list(map(lambda polygon: tr_homothety(polygon, i * 0.1), j)) for i, j in enumerate(c)]
a = [list(map(lambda polygon: (-polygon[0] - 0.4, -polygon[1]), i)) for i in b]
b = list(filter(lambda polygon: flt_square(0.5, polygon), b))
a = list(filter(lambda polygon: flt_square(0.5, polygon), a))
#visual_inf(a, b)  # Пункт 1

a = generate_figure(gen_rectangle((0, 0), 3, 2, 4, 0), 15)
b = [list(map(lambda polygon: tr_homothety(polygon, 1 + i * 0.1), j)) for i, j in enumerate(a)]
b = list(filter(lambda polygon: flt_short_side(3, polygon), b))

visual_inf(b)  # Пункт 2

a = generate_figure(gen_rectangle((0, 0), 3, 2, 4, 0), 7)
b = generate_figure(gen_rectangle((10, -5), 3, 2, 0, 4), 7)
a = list(filter(lambda polygon: flt_point_inside((12.5, 0.5), polygon), a))
b = list(filter(lambda polygon: flt_point_inside((12.5, 0.5), polygon), b))
a = list(filter(lambda polygon: flt_point_inside((8.5, 0.5), polygon), a))
#visual_inf(a, b)  # Пункт 3
