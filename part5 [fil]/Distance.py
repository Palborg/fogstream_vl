""" В одном файле в каждой строке записаны координаты пар точек. 
Каждая координата отделена от другой пробелом. 
Например, строка вида 3 6 -2 4 означает, 
что координаты первой точки (3;6), второй - (-2;4). 
Во второй файл требуется построчно записать наибольшее и
наименьшее расстояние между точками.

"""
def distance(x1,y1,x2,y2):
    
    return [((x2 - x1)**2 + (y2 - y1)**2)**0.5, abs(x1 - x2) + abs(y1 - y2)]


lst = []
with open('input2.txt', 'r') as f:
    a = f.read()
    a = a.split()
    for i in a:
        lst.append(int(i))
lst = distance(lst[0], lst[1], lst[2], lst[3])
with open('output2.txt', 'w') as f:
    f.write('Наибольшее расстояние: ' + str(lst[1]) + '\nНаименьшее расстояние: ' + str(lst[0]))


