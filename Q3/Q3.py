import turtle
ninja = turtle.Turtle()

# Recursive function to draw a single modified edge
def drawEdges (length, depth ):
    if depth == 0:
        ninja.forward(length)
    else:
        length /= 3
        drawEdges(length, depth -1)
        ninja.left(60)
        drawEdges(length, depth -1)
        ninja.right(120)
        drawEdges(length, depth -1)
        ninja.left(60)
        drawEdges(length, depth -1)

# ------------ Function to draw a polygon ---------
def drawPolygon(sides, length, depth):
    angle = 360 / sides
    for _ in range(sides):
        drawEdges(length, depth)
        ninja.left(angle)

#------ Main Program ----------
def main():

# --------- User Input ------------
    sides=int(input("enter the number of sides:"))
    length= int(input("enter the side length"))
    depth= int(input("enter the recursion depth:"))

    #----- Setting Turtle ----------
    ninja.speed(0)
    ninja.shape("turtle")
    turtle.bgcolor("black")
    ninja.color("green")

    #-------- Center the shape -----------
    ninja.penup()
    ninja.goto(-length/2, -length/2)
    ninja.pendown()

    drawPolygon(sides, length, depth)

    turtle.done ()

main()