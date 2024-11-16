import turtle

# creating canvas
turtle.Screen().bgcolor("Orange")

sc = turtle.Screen()
sc.setup(400, 300)



# turtle object creation
board = turtle.Turtle()

# creating a square
for p in range(4):
	board.forward(100)
	board.left(90)
	p = p+1