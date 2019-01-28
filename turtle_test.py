import turtle

#Window-----------
wn=turtle.Screen()
wn.bgcolor('green')


#Turtles----------
alex=turtle.Turtle()

degrees=int(input("How many degrees for Bob to turn? "))
change=int(input("How many degrees to change? "))
how_far=int(input("How far for Bob to move? "))
many=int(input("How many times? "))
spd=int(input("How fast? "))
color=input("Color? ")
sz=int(input("How big? "))

alex.pensize(sz)
alex.color(color)
alex.speed(spd)
for x in range(many):
    alex.rt(degrees)
    degrees+=change
    alex.fd(how_far)

wn.exitonclick()
