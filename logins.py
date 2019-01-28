
#variables

user='bob'
pw='password'
#user entries

def login(user,pw,tries):
    if tries==0:
        print('Too bad')
        quit()
        
    u_entry=input('User: ')
    pw_entry=input('Password: ')
    #functions
    if u_entry==user and pw_entry==pw:
        print('Logged in!')
    else:
        print('Incorrect')
        tries-=1

        print("You only have %i tries left"%tries)
        
        login(user,pw,tries)
    
login(user,pw,3)

