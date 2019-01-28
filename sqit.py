#HCD Return Testing
def square(x):
    sq=x*x
    return sq

def check_it():
    num=float(input("What number do you want to square? "))
    num_sq=square(num)
    print("Your number squared is %f"%num_sq)
    again=input("Do you want to do again? ").lower()
    if again=="yes" or again=="y":
        check_it()
    else:
        quit()
        
check_it()
