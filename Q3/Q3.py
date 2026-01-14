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

def main():
    
    sides=int(input("enter the number of sides:"))
    length= int(input("enter the side length"))
    depth= int(input("enter the recursion depth:"))

    turtle.done ()

main()