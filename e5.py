def pertence(letras, x):
    for i in letras:
        if x == i:
            return True
    
    return False

def isIsogram(x):
    letras = []
    for i in x:
        if i.isalpha():
            if(not pertence(letras,i)):
                letras.append(i)
            else: return False
    return True

def main():
    palavra = input()
    if(isIsogram(palavra)): print('isogram')
    else: print('not')

main()