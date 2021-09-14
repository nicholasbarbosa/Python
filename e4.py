def bi(y):
    if(y % 4 == 0 and y % 100 != 0):
        return True

    if(y % 4 == 0 and y % 400 == 0):
        return True
   
    if(y % 100 == 0):
        return False
    
    return False

def main():
    y = int(input())

    if(bi(y)):
        print("bissexto")
    else:
        print("nao é")

main()