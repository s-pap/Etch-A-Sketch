#etch_a_sketch
import turtle

wn=turtle.Screen()
wn.title("Etch A Sketch Coded by Sarah")
wn.bgcolor("white")
wn.setup(width=800, height=600)

t=turtle.Pen()
t.speed(0)
t.turtlesize(2,2,2)

pen1=turtle.Pen()
pen1.penup()
pen1.hideturtle()
pen1.speed(0)
pen1.goto(0, -250)
pen1.write("Press [SPACE] to clear", align="center", font=("Courier", 20,"normal" ))

pen2=turtle.Pen()
pen2.penup()
pen2.hideturtle()
pen2.speed(0)
pen2.goto(0, 250)
pen2.write("Etch A Sketch", align="center", font=("Courier", 24,"normal" ))

def up():
    t.setheading(90)
    t.forward(20)
def right():
    t.setheading(0)
    t.forward(20)
def down():
    t.setheading(270)
    t.forward(20)
def left():
    t.setheading(180)
    t.forward(20)
def clear():
    t.clear()
    t.penup()
    t.goto(0,0)
    t.pendown()

wn.listen()
turtle.onkeypress(up, "Up")
turtle.onkeypress(right, "Right")
turtle.onkeypress(left, "Left")
turtle.onkeypress(down, "Down")
turtle.onkeypress(clear, "space")
    
    
