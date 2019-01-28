code=""
planet=""
name=""
score=0
def welcome():   
    global name
    print("Hello! Welcome to the Spaceship game!") 
    print("---------------------------------------------------------------------------------")
    print("                          `. ___ ")
    print("                         __,' __`.                _..----....____ ")
    print("              __...--.'``;.   ,.   ;``--..__     .'    ,-._    _.-' ")
    print("        _..-''-------'   `'   `'   `'     O ``-''._   (,;') _,' ")
    print("      ,'________________                          \`-._`-',' ")
    print("      `     ._              ```````````------...___   '-.._'-: ")
    print("        ```--.._      ,.                     ````--...__\-.  ")
    print("               `.--. `-`                       ____    |  |` ")
    print("                 `. `.                       ,'`````.  ;  ;` ")
    print("                   `._`.        __________   `.      \'__/` ")
    print("                      `-:._____/______/___/____`.     \  ` ")
    print("                                  |       `._    `.    \ ")
    print("                                  `._________`-.   `.   `.___")
    print("                                                     `------") 
    print("---------------------------------------------------------------------------------")
    print("The objective of the game is to fly from one planet to another without dying.")
    print("---------------------------------------------------------------------------------")
    name=input("What is your name?   ")
    usermenu()
def planet_code():
    global code
    code=(input("Enter Code:   "))
    if code=="1":
        escape_earth()      
    elif code=="2":
        escape_mercury()
    elif code=="3":
        escape_venus()
    elif code=="4":
        escape_mars()
    elif code=="5":
        escape_jupiter()
    elif code=="6":
        escape_saturn()
    elif code=="7":
        escape_uranus()
    elif code=="8":
        escape_neptune()
    elif code=="9":
        escape_pluto()
    else:
        print("Invalid Code...")
        usermenu()
def usermenu():
    global code
    option=input(""" What do you want to do?
        Press "1" to Start Game :     
        Press "2" to Enter Planet Code :        
        Press "3" to Exit the Game :
        """)
    if option=="1":
        weight=float(input("How heavy is the ship?   "))
        escape_earth()
    elif option=="2":
        planet_code()
        
    elif option == "3":
        print("Exiting Game...")
        exit()
    else:
        print("Invalid Entry")
        usermenu()

def escape_planet():
    global planet
    if planet=="earth":
        escape_earth()
    if planet=="mercury":
        escape_mercury()    
    if planet=="venus":
        escape_venus()
    if planet=="mars":
        escape_mars()
    if planet=="jupiter":
        escape_jupiter()
    if planet=="saturn":
        escape_saturn()
    if planet=="uranus":
        escape_uranus()
    if planet=="neptune":
        escape_neptune()
    if planet=="pluto":
        escape_pluto()
def escape_earth():
    global planet
    global name
    global score
    planet="earth"
    score=score+0
    print("You are now on Earth")
    print("The Planet Code is: 1")
    print ("Your score is",score)
    speed=float(input("How fast do you want to go?   "))
    location=input("What planet do you want to go?   ").lower()
    if planet=="earth":
        if speed>=11.186 and speed<=12.3046:
            print("Well Done!", name,"! You successfully bypassed the atmosphere on Earth!")
            planet=location
            print("You gained 10 points")
            escape_planet()
        elif speed>12.3046:
            print("You went too fast and crashed...")
            print("You scored",score)
            usermenu()
        elif speed<11.186:
            print("You went too slow and crashed...")
            print("You scored",score)
            usermenu()
    escape_planet()
def escape_mercury():
    global planet
    global name
    global score
    score= score +10
    planet="mercury"    
    print("You are now on Mercury")
    print("The Planet Code is: 2")
    print ("Your score is",score)
    speed=float(input("How fast do you want to go?   "))
    location=input("What planet do you want to go to?   ").lower()
    if planet=="mercury":
        if speed>=4.25 and speed<=4.675:
            print("Well done", name,"! You successfully bypassed the atmosphere on Mercury.")
            planet=location
            print("You gained 10 points")
            escape_planet()
        elif speed>4.675:
            input("You went too fast and crashed...")
            print("You scored",score)
            usermenu()
        elif speed<4.25:
            input("You went too slow and crashed...")
            print("You scored",score)
            usermenu()
    escape_planet()
def escape_venus():
    global planet
    global name
    global score
    score= score +10
    planet="venus"
    print("You are now on Venus")
    print("The Planet Code is: 3")
    print ("Your score is",score)
    speed=float(input("How fast do you want to go?   "))
    location=input("What planet do you want to go?   ").lower()
    if planet=="venus":
        if speed>=10.36 and speed<=11.396:
            print("Well Done!", name,"! You successfully bypassed the atmosphere on Venus!")
            planet=location
            print("You gained 10 points")
            escape_planet()
        elif speed>11.396:
            print("You went too fast and crashed...")
            print("You scored",score)
            usermenu()
        elif speed<10.36:
            print("You went too slow and crashed...")
            print("You scored",score)
            usermenu()
    escape_planet()
def escape_mars():
    global planet
    global name
    global score
    score= score +10
    planet="mars"
    print("You are now on Mars")
    print("The Planet Code is: 4") 
    print ("Your score is",score)
    speed=float(input("How fast do you want to go?   "))    
    location=input("What planet do you want to go?   ").lower()
    if planet=="mars":
        if speed>=5.03 and speed<=5.533:
            print("Well Done!", name,"! You successfully bypassed the atmosphere on Mars!")
            planet=location
            print("You gained 10 points")
            escape_planet()
        elif speed>5.533:
            print("You went too fast and crashed...")
            print("You scored",score)
            usermenu()
        elif speed<5.03:
            print("You went too slow and crashed...")
            print("You scored",score)
            usermenu()
    escape_planet()
def escape_jupiter():
    global planet
    global name
    global score
    score= score +10
    planet="jupiter"
    print("You are now on Jupiter")
    print("The Planet Code is: 5")
    print ("Your score is",score)
    speed=float(input("How fast do you want to go?   "))
    location=input("What planet do you want to go?   ").lower()
    if planet=="jupiter":
        if speed>=60.2 and speed<=66.22:
            print("Well Done!", name,"! You successfully bypassed the atmosphere on Jupiter!")
            planet=location
            print("You gained 10 points")
            escape_planet()
        elif speed>66.22:
            print("You went too fast and crashed...")
            print("You scored",score)
            usermenu()
        elif speed<60.2:
            print("You went too slow and crashed...")
            print("You scored",score)
            usermenu()
    escape_planet()
def escape_saturn():
    global planet
    global name
    global score
    score= score +10
    planet="saturn"
    print("You are now on Saturn")
    print("The Planet Code is: 6")
    print ("Your score is",score)
    speed=float(input("How fast do you want to go?   "))
    location=input("What planet do you want to go?   ").lower()
    if planet=="saturn":
        if speed>=36.09 and speed<=39.699:
            print("Well Done!", name,"! You successfully bypassed the atmosphere on Saturn!")
            planet=location
            print("You gained 10 points")
            escape_planet()
        elif speed>39.699:
            print("You went too fast and crashed...")
            print("You scored",score)
            usermenu()
        elif speed<36.09:
            print("You went too slow and crashed...")
            print("You scored",score)
            usermenu()
    escape_planet()
def escape_uranus():
    global planet
    global name
    global score
    score= score +10
    planet="uranus"
    print("You are now on Uranus")
    print("The Planet Code is: 7")
    print ("Your score is",score)
    speed=float(input("How fast do you want to go?   "))
    location=input("What planet do you want to go?   ").lower()
    if planet=="uranus":
        if speed>=21.38 and speed<=23.518:
            print("Well Done!", name,"! You successfully bypassed the atmosphere on Uranus!")
            planet=location
            print("You gained 10 points")
            escape_planet()
        elif speed>23.518:
            print("You went too fast and crashed...")
            print("You scored",score)
            usermenu()
        elif speed<21.38:
            print("You went too slow and crashed...")
            print("You scored",score)
            usermenu()
def escape_neptune():
    global planet
    global name
    global score
    score= score +10
    planet="neptune"
    print("You are now on Neptune")
    print("The Planet Code is: 8")
    print ("Your score is",score)
    speed=float(input("How fast do you want to go?   "))
    location=input("What planet do you want to go?   ").lower()
    if planet=="neptune":
        if speed>=23.56 and speed<=25.916:
            print("Well Done!", name,"! You successfully bypassed the atmosphere on Neptune!")
            planet=location
            print("You gained 10 points")
            escape_planet()
        elif speed>25.196:
            print("You went too fast and crashed...")
            print("You scored",score)
            usermenu()
        elif speed<23.56:
            print("You went too slow and crashed...")
            print("You scored",score)
            usermenu()
    escape_planet()
def escape_pluto():
    global planet
    global name
    global score
    score= score +10
    planet="pluto"
    print("You are now on Pluto")
    print("The Planet Code is: 9")
    print ("Your score is",score)
    speed=float(input("How fast do you want to go?   "))
    location=input("What planet do you want to go?   ").lower()
    if planet=="pluto":
        if speed>=1.23 and speed<=1.353:
            print("Well Done!", name,"! You successfully bypassed the atmosphere on Pluto!")
            planet=location
            print("You gained 10 points")
            escape_planet()
        elif speed>1.353:
            print("You went too fast and crashed...")
            print("You scored",score)
            usermenu()
        elif speed<1.23:
            print("You went too slow and crashed...")
            print("You scored",score)
            usermenu()
    escape_planet()
welcome()
