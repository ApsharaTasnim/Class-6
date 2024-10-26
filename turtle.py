import turtle

turtle.Screen().bgcolor("Orange")


sc=turtle.Screen()
sc.setup(300,400)

turtle.title("Welcome to the turtle window!")
board=turtle.Turtle()

for i in range(6):
   board.forward(70)
   board.left(60)
   i=i+1


