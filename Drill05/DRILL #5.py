import turtle

def turtle_move_W():    #위
    turtle.stamp()
    turtle.setheading(90)
    turtle.forward(50)
    
def turtle_move_A():    #왼쪽
    turtle.stamp()
    turtle.setheading(180)
    turtle.forward(50)
    
def turtle_move_S():    #아래
    turtle.stamp()
    turtle.setheading(270)
    turtle.forward(50)
    
def turtle_move_D():    #오른쪽
    turtle.stamp()
    turtle.setheading(0)
    turtle.forward(50)

def Restart():          #재시
    turtle.reset()

turtle.shape('turtle')

turtle.onkey(turtle_move_W, 'w')
turtle.onkey(turtle_move_A, 'a')
turtle.onkey(turtle_move_S, 's')
turtle.onkey(turtle_move_D, 'd')
turtle.onkey(Restart, 'Escape')

turtle.listen()
