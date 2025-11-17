import math
def calculate_rectangle_area(weigth, height):
    """вычисляет площадь прямоугольника
    Args:
        width, height (float): размеры прямоугольника
    returns:
        float: площадь прямоугольника"""
    area = weight * height
    return area
def calculate_circle_area(radius):
    """вычисляет радиус круга
    Args:
        radius (float): радиус круга
    returns:
        float: радиус круга"""
    area = 2 * math.pi * radius
    return area
weight, height = map(float, input("введите высоту и ширину прямоугольника(через пробел)").split())
print(calculate_rectangle_area(weight, height))

radius = float(input("Введите радиус круга"))
print(calculate_circle_area(radius))
