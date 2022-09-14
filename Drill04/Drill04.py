import turtle

turtle.penup()
turtle.goto(-100,-100)
turtle.pendown()
turtle.setheading(0)

movecount = 0
count = 0
while 1:
    if count == 5:
        turtle.left(90)
        turtle.forward(100)
        turtle.left(90)
        turtle.forward(500)
        turtle.left(180)
        movecount = movecount + 1
        count = 0
        if movecount == 5:
            break;
        
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    count = count + 1



