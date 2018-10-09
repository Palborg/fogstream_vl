# Написать функцию is_prime, принимающую 1 аргумент - число от 0 до 1000, и 
# возвращающую True, если оно простое, и False - иначе
a = int(input())

def is_prime(n) :
    for i in range(2, n-1) : 
        if n % i == 0 :
            return False

    return True
    
print(is_prime(a))

       
            
    


