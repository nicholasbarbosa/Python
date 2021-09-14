def degenerate(a,b,c):
    if(a + b == c):
        return True
    if(b + c == a):
        return True
    if(a + c == b):
        return True
    
    return False

def triangle(a, b, c):
    if(a <= 0 or b <= 0 or c <= 0):
        return False

    if(a + b >= c and b + c >= a and a + c >= b):
        return True
    else: return False

def tipo(a, b, c):
    if(a == b == c):
        return 'Equilatero'
    
    if(a == b or a == c or c == b):
        return 'Isoceles'
    
    return 'Escaleno'

def main():
    a = int(input())
    b = int(input())
    c = int(input())

    if(triangle(a,b,c)):
        print('é triangulo')
        if(degenerate(a,b,c)): print('degenerado')
        else: print('nao é degenerado')

        print(tipo(a,b,c))

    
main()
    