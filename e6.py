def case(x):
    for i in range(0,len(x)):
        if not x[i].isupper():
            return False
    
    return True

def answers(q):
    print(len(q))

    if q == 'How are you?':
        return 'Sure'
    
    elif case(q) and len(q) > 0:
        return 'Whoa, chill out!'

    elif len(q) > 0 and q[len(q)-1] == '?':
        return 'Calm down, i know what im doing!'
    
    elif len(q) == 0:
        return 'Fine. be that way!'
    
    else:
        return 'Whatever'

def main():
    q = input()
    print(answers(q))

main()