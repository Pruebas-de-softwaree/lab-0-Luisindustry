def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    
    return a / b  

def power(a, b):
    return a ** b  

def square_root(x):
    import math
    return math.sqrt(x)

def average(list):
    return sum(list) / len(list)

def maximum(list):
    return max(list) 


if __name__ == "__main__":

    print("start test")
    
    print(" Se modificó la formula de 'min' a 'Max', corrigiendo los errores ")
    print(maximum([9,7,5]))
    print(maximum(['u','4','6']))

    print("end test")

