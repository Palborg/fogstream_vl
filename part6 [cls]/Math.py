""" Создать класс Fraction, который должен иметь два поля: 
числитель a и знаменатель b. 
Оба поля должны быть типа int. 
Реализовать методы: 
сокращение дробей, сравнение, сложение и умножение.

"""

class Fraction:
    
    def __init__(self, a, b):
        self.a = int(a)
        self.b = int(b)
    
    def take_main(self):
        return self.a//self.b
    
    def sum(self):
        return self.a + self.b
    
    def mult(self):
        return self.a*self.b

n = input().split()
cl = Fraction(n[0], n[1])
print('Результат деления без дробной части: ', cl.take_main())
print('Результат сложения: ', cl.sum())
print('Результат умножения: ', cl.mult())