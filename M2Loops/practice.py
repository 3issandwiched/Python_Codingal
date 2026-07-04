# as you already know turtle is  library

import turtle

# create object of the turtle

t = turtle.Turtle() # you ll understand later in object oriented programming.


for i in range(0,3):
    t.forward(250)
    t.left(120)
    
t.penup()
t.left(90)
t.forward(120)
t.right(90)
t.pendown()

for i in range(0,3):
    t.forward(250)
    t.right(120)

turtle.done() # freeze the screen.