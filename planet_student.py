#Space Shuttle

import time, sys
USER=""
PLANET=""
SCORE=0
total=""
E1=""
M1=""
V1=""
M2=""
J1=""
S1=""
U1=""
N1=""




def greeting():
    global USER
    print("""Hello captain! you are piloting the spaceship Aroura,renowned throughout the    solar system as one of the most advanced ships in the milky way, and you young  pilot, have been chosen to be captain!""")
    USER=input("So tell me captain, what's your name? : ")
    menu()
def menu():
    global USER
    global PLANET
    global SCORE
    global E1
    global M1
    global V1
    global M2
    global J1
    global S1
    global U1
    global N1


    print("Pleasure to meet you captain %s"%USER)
    print("""are you ready to board the Arora captain %s:"""%USER)
    c=input("""
    1. Start Game
    2. Enter Planet Code
    : """)
    if c=='1':
        weight=input("What do you want the Arora's weight to be: ")
        PLANET="earth"
        planet()
    elif c=='2':
        code=input("Planet code: ")

        if code == E1:

            PLANET=earth
            planet()

        elif code == M1:
            PlANET=mercury
            planet()

        elif code == V1:
            PLANET=venus
            planet()

        elif code == M2:
            PLANET=mars
            planet()

        elif code == J1:
            PLANET=jupiter
            planet()

        elif code == S1:
            PLANET=saturn
            planet()

        elif code == U1:
            PLANET==uranus
            planet()

        elif code == N1:
            PLANET=neptune
            planet()

    else:
        print('Invalid entry')
        menu()

def quit_option():
    quit1=input("Are you sure you want to quit? ")
    if quit1=="yes" or quit1=="Yes":
        quit()
    else:
        menu()



def planet():
    global USER
    global PLANET
    global SCORE
    global total
    global E1
    global M1
    global V1
    global M2
    global J1
    global S1
    global U1
    global N1
    speed =float( input("what speed do you think the arora should be going at to escape the atmosphere of %s captain?(mi/H) :"%PLANET))
    print("Your score is currantly %i "%SCORE)
    chose=input('planet ')
    if PLANET == "earth":
        if speed>=25000 and speed<=27000:
            PLANET=chose
            SCORE+=300
            print("congrats! you have safly landed the arora on %s surface."%PLANET)
            print("the planet code for %s is E1")
            planet()
        elif speed>27000:
            print("captain! i think we're going too fast! the hull is desintigrating! CAPT-")
            planet()
        elif speed<25000:
            print("captain! i think we're going too slow! we're about to crash! CAPT-")
        else:
            print("i messed up...")
            planet()


    elif PLANET == "mercury":
        if speed>=9618 and speed<=11618:
            PLANET=chose
            print("congrats! you have safly landed the arora on %s surface."%PLANET)
            print("the planet code for %s is M1")
            SCORE+=100
            planet()
        elif speed>11618:
            print("captain! i think we're going too fast! the hull is desintigrating! CAPT-")
            planet()
        elif speed<9618:
            print("captain! i think we're going too slow! we're about to crash! CAPT-")
        else:
            print("i messed up...")
            planet()
     
    elif PLANET == "venus":
        if speed>=23174 and speed<=25174:
            PLANET=chose
            print("congrats! you have safly landed the arora on %s surface."%PLANET)
            print("the planet code for %s is V1")
            SCORE+=200
            planet()
        elif speed>25174:
            print("captain! i think we're going too fast! the hull is desintigrating! CAPT-")
            planet()
        elif speed<23174:
            print("captain! i think we're going too slow! we're about to crash! CAPT-")
        else:
            print("i messed up...")
            planet() 

    elif PLANET == "mars":
        if speed>=11000 and speed<=13000:
            PLANET=chose
            print("congrats! you have safly landed the arora on %s surface."%PLANET)
            print("the planet code for %s is M2")
            SCORE+=400
            planet()
        elif speed>13000:
            print("captain! i think we're going too fast! the hull is desintigrating! CAPT-")
            planet()
        elif speed<11000:
            print("captain! i think we're going too slow! we're about to crash! CAPT-")
        else:
            print("i messed up...")
            planet()


    elif PLANET == "jupiter":
        if speed>=131979 and speed<=133979:
            PLANET=chose
            print("congrats! you are safly hovering the arora in %s surface."%PLANET)
            print("the planet code for %s is J1")
            SCORE+=500
            planet()
        elif speed>133979:
            print("captain! i think we're going too fast! the hull is desintigrating! CAPT-")
            planet()
        elif speed<131979:
            print("captain! i think we're going too slow! we're about to get sucked into the red eye! CAPT-")
        else:
            print("i messed up...")
            planet()


    elif PLANET == "saturn":
        if speed>=78292 and speed<=81292:
            PLANET=chose
            print("congrats! you are safly hovering the arora in %s surface."%PLANET)
            print("the planet code for %s is S1")
            SCORE+=600
            planet()
        elif speed>81292:
            print("captain! i think we're going too fast! the hull is desintigrating! CAPT-")
            planet()
        elif speed<78292:
            print("captain! i think we're going too slow! we're about to get hit by saturns rings! CAPT-")
        else:
            print("i messed up...")
            planet()

    elif PLANET == "uranus":
        if speed>=46975 and speed<=49975:
            PLANET=chose
            print("congrats! you are safly hovering the arora in %s surface."%PLANET)
            print("the planet code for %s is U1")
            SCORE+=700
            planet()
        elif speed>49975:
            print("captain! i think we're going too fast! the hull is desintigrating! CAPT-")
            planet()
        elif speed<46975:
            print("captain! i think we're going too slow! we're about to get enveloped by the misty blue storm we'll call our GRAVE! CAPT-")
        else:
            print("i messed up...")
            planet()

    elif PLANET == "neptune":
        if speed>=52568 and speed<=55568:
            PLANET=chose
            print("congrats! you are safly hovering the arora in %s surface."%PLANET)
            print("the planet code for %s is N1")
            SCORE+=800
            planet()
        elif speed>55568:
            print("captain! i think we're going too fast! the hull is desintigrating! CAPT-")
            planet()
        elif speed<52568:
            print("captain! i think we're going too slow! we're about to get enveloped by the sea of ozone blue gas that will suffocate us slowly and painfully untill we hit the core and get OBLITERATED! CAPT-")
        else:
            print("i messed up...")
            planet()
    else:
        print('Incorrect entry ')
        planet()
greeting()
