from math import pi, pow, sqrt

def get_area(a, b=None, c=None):
    #круг#
    if type_figure(a, b, c) == "circle": 
        return pi * pow(a, 2)
     #треугольник#
    elif type_figure(a, b, c) == "trangle":
        p = (a + b + c) / 2
        return sqrt(p * (p - a) * (p - b) * (p - c))
    

def type_figure(a, b=None, c=None):

    if b is None and c is None and a > 0:
        return "circle"
    
    elif b is not None and c is not None and a + b > c and b + c > a and c + a > b:
        return "trangle"
    #сюда можно добавить другие фигуры
    else:
        raise ValueError('Некорректные параметры фигуры')