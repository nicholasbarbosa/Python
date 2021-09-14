def collatz(n):
    resp = 0
    while n != 1:
        if(n % 2 == 0):
            n /= 2
            resp += 1
        
        else:
            n *= 3
            n += 1
            resp += 1
    
    return resp

def main():
    n = int(input())
    print(collatz(n))

main()