import turtle
from turtle import *
from random import randint

wn=turtle.Screen()
wn.title("Turtle Race")
wn.bgcolor("lightgreen")

for step in range(9):
    write(step, align='center')
    right(90)
    forward(10)
    pendown()   #moves the turtle and leave track
    forward(150)
    penup()         #we cannot see the line in penup moves the turtle
    backward(160)
    left(90)
    forward(20)
    speed(40)

blue = Turtle()
blue.color('blue')
blue.shape('turtle')
blue.penup()
blue.goto(-100,-40)
blue.pendown()

red=Turtle()
red.color('red')
red.shape('turtle')
red.penup()
red.goto(-100,-20)
red.pendown()

green=Turtle()
green.color('green')
green.shape('turtle')
green.penup()
green.goto(-100,-60)
green.pendown()

yellow=Turtle()
yellow.color('orange')
yellow.shape('turtle')
yellow.penup()
yellow.goto(-100,-80)
yellow.pendown()

black=Turtle()
black.color('black')
black.shape('turtle')
black.penup()
black.goto(-100,-100)
black.pendown()

purple=Turtle()
purple.color('purple')
purple.shape('turtle')
purple.penup()
purple.goto(-100,-120)
purple.pendown()

pink=Turtle()
pink.color('pink')
pink.shape('turtle')
pink.penup()
pink.goto(-100,-140)
pink.pendown()


for turn in range(60):
    red.forward(randint(0,9))
    blue.forward(randint(0,9))
    green.forward(randint(0,9))
    yellow.forward(randint(0,9))
    black.forward(randint(0,9))
    purple.forward(randint(0,9))
    pink.forward(randint(0,9))

wn.exitonclick()
