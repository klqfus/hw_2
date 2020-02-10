import turtle
from rectangle import rectangle


def nested_rectangle(n):
    c = ['red', 'blue', 'green']
    for i in range(n):
        rectangle(10 + 10+i)
        turtle.penup()
        turtle.color(c[i])
        turtle.goto(-5*i, -5*i)
        turtle.pendown()

if __name__ =="__main__":
    for i in range(1, 10, 2):
        nested_rectangle(5)