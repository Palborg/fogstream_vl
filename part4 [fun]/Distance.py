# Даны четыре действительных числа: x1, y1, x2, y2. Напишите функцию 
# distance(x1, y1, x2, y2), вычисляющая расстояние между точкой (x1,y1) и 
# (x2,y2). Считайте четыре действительных числа и выведите результат работы 
# этой функции.
from math import sqrt

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

def distance(x1, y1, x2, y2) :
    return round(sqrt(abs(x2 - x1) ** 2 + abs(y2 - y1) ** 2),5)

print(distance(x1, y1, x2, y2))
