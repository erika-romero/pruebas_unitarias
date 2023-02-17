"""
Your module description
"""
def sumar(x,y):
    return x+y
    
print(sumar(2,4))


def primo(num, n=2):
    if n >= num:
        print("Es primo")
        return True
    elif num % n != 0:
        return primo(num, n + 1)
    else:
        print("No es primo", n, "es divisor")
        return False
print(primo(3))