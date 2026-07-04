import turtle

# creating canvas
turtle.Screen().bgcolor("Orange")

sc = turtle.Screen()
sc.setup(400, 300)

turtle.title("Welcome to Turtle Window")

# turtle object creation
board = turtle.Turtle()

# creating a square
for i in range(4):
	board.forward(100) #Move the turtle forward by 100 units
	board.left(90) #Angle of 90 degree is used to create a square
	i = i+1
