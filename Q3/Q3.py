import turtle
ninja = turtle.Turtle()

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

turtle.done ()