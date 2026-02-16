#TurtleGraphics.py
#Name: Mariana Chavez  
#Date: 02.15.2026
#Assignment:Lab 4

import turtle #needed generally but not in CodeHS
hideturtle() #hides the default turtle in CodeHS

def drawSquare(myTurtle, size):
    for i in range(4):
        myTurtle.forward(size)
        myTurtle.right(90)
   
def drawPolygon(bob, sides):
    for s in range(sides):
        bob.forward(50)
        bob.right(360/sides)
    
def fillCorner(alice, corner):
    #draw big square
    drawSquare(alice, 100)
    
    if corner == 1:
        alice.begin_fill()
        drawSquare(alice, 50)
        alice.end_fill()
    elif corner == 2:
        alice.forward(50)
        alice.begin_fill()
        drawSquare(alice, 50)
        alice.end_fill()
    elif corner == 3:
        alice.goto(0, -50)
        alice.begin_fill()
        drawSquare(alice, 50)
        alice.end_fill()
    elif corner == 4:
        alice.penup()
        alice.goto(50,-50)
        alice.pendown()
        alice.begin_fill()
        drawSquare(alice, 50)
        alice.end_fill()
        
def squaresInSquares(sheldon, num):
    increment = 20
    
    for i in range(num):
        size = 50 + (i * increment)
        
        sheldon.penup()
        sheldon.goto(0, 0)
        sheldon.setheading(0)
        sheldon.backward(size / 2)
        sheldon.left(90)
        sheldon.forward(size / 2)
        sheldon.right(90)
        sheldon.pendown()
        
        drawSquare(sheldon, size)
        

def main():
    myTurtle = turtle.Turtle()
    
    # drawSquare(myTurtle, 100)
    
    # drawPolygon(myTurtle, 5) #draws a pentagon
    # drawPolygon(myTurtle, 8) #draws an octogon
    # drawPolygon(myTurtle, 3) #draws a triangle
    

    # fillCorner(myTurtle, 2) #draws a square with top right corner filled in.
    # fillCorner(myTurtle, 3) #draws a square bottom left corner filled in.

    squaresInSquares(myTurtle, 5) #draws 5 concentric squares
    # squaresInSquares(myTurtle, 3) #draws 3 concentric squares


main()
