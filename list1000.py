names=['john','jane','ismail','amani']

def get_name(n):
    new=input('What is your name? ')
    n.append(new)
    ask=input('Another name? ')
    if ask=='yes' or ask=='y':
        print(n)
        get_name(n)
    return n

final=get_name(names)
print(final)
