from math import pi, pow, sqrt


def get_area(a, b=None, c=None):
    # Круг#
    if type_figure(a, b, c) == "circle":
        return pi * pow(a, 2)
    # Треугольник#
    elif type_figure(a, b, c) == "trangle" or type_figure(a, b, c) == "right trangle":
        p = (a + b + c) / 2
        return sqrt(p * (p - a) * (p - b) * (p - c))


def type_figure(a, b=None, c=None):

    if b is None and c is None and a > 0:
        return "circle"
    elif b is not None and c is not None and a + b > c and b + c > a and c + a > b:
        if pow(a, 2) + pow(b, 2) == pow(c, 2) or pow(c, 2) + pow(b, 2) == pow(a, 2) or pow(a, 2) + pow(c, 2) == pow(b, 2):
            return "right trangle"
        return "trangle"
    # Сюда можно добавить другие фигуры
    else:
        raise ValueError('Некорректные параметры фигуры')
