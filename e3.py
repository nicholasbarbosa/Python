def raindrop(n):
    resp = ''
    if(n % 3 == 0):
        resp += 'Pling'
    
    if(n % 5 == 0):
        resp += 'Plang'

    if(n % 7 == 0):
        resp += 'Plong'
    
    if(len(resp) == 0):
        resp = str(n)

    return resp

def main():
    n = int(input())
    print(raindrop(n))

main()

