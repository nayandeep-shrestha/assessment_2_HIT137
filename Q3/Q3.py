import turtle

# Recursive function to draw a single modified edge


def drawEdges(t, length, depth):
    if depth == 0:  # base case drawing a straight line
        t.forward(length)
    else:  # recursive case divided into 4 segments
        length /= 3
        drawEdges(t, length, depth - 1)
        t.left(60)
        drawEdges(t, length, depth - 1)
        t.right(120)
        drawEdges(t, length, depth - 1)
        t.left(60)
        drawEdges(t, length, depth - 1)

# ------------ Function to draw a polygon ---------


def drawPolygon(t, sides, length, depth):
    angle = 360 / sides
    for _ in range(sides):
        drawEdges(t, length, depth)
        t.left(angle)

# ------ Main Program ----------


def main():

    # --------- User Input ------------
    sides = int(input("enter the number of sides:"))
    length = int(input("enter the side length"))
    depth = int(input("enter the recursion depth:"))

    # ----- Setting Turtle ----------
    screen = turtle.Screen()
    screen.bgcolor("black")
    t=turtle.Turtle()
    t.speed(0)
    t.shape("turtle")
    turtle.bgcolor("black")
    t.color("green")

    # -------- Center the shape -----------
    t.penup()
    t.goto(-length/2, -length/2)
    t.pendown()

    # ------ Generate the pattern ----------
    drawPolygon(t,sides, length, depth)

    turtle.done()


main()
