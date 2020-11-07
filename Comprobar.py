def esprimo(n):
    if n<2:
        return False
    else:
        for i in range(2,n):
            if n%i == 0:
                return False
        return True
        
def factorial(n):
    B=1
    for i in range(1,n+1):
        B=i*B
    return B