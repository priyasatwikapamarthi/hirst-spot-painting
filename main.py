import turtle
from turtle import Turtle,Screen
turtle.colormode(255)
import random

colours = [(62, 95, 129), (128, 177, 134), (115, 77, 87), (205, 165, 96), (113, 163, 203), (227, 210, 100), (192, 140, 152), (67, 116, 69), (180, 96, 114), (135, 83, 59), (182, 165, 42), (224, 86, 79), (60, 47, 53), (175, 203, 182), (234, 158, 169), (80, 55, 68), (239, 174, 157), (39, 55, 71), (96, 144, 150), (107, 150, 114), (46, 61, 95)]
timmy = Turtle()
timmy.speed("fast")
timmy.hideturtle()
timmy.penup()
timmy.setheading(225)
timmy.fd(350)
timmy.setheading(0)
original_x = timmy.xcor()
original_y = timmy.ycor()
x = timmy.xcor()
y = timmy.ycor()
dots = 0
while not dots == 100 :

    timmy.dot(20,random.choice(colours))
    timmy.penup()
    x += 50
    if x==500+original_x :
        y = y+50
        x = original_x
    timmy.setpos(x,y)
    timmy.pendown()
    dots += 1


screen = Screen()
screen.exitonclick()


