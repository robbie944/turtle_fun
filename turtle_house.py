#Turtle fun
#By Robin Chandler
#function to draw a house
import turtle
def square (length):
    for l in range(4):
        turtle.color("red")
        turtle.width(5)
        turtle.forward(length)
        turtle.right(90)
        turtle.speed(0)

def triangle (length):
    for i in range (3):
        turtle.color("red")
        turtle.width(5)
        turtle.forward(length)
        turtle.left(120)
       # turtle.speed(0)
        turtle.width(5)
square(150)
triangle(150)
