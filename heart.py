import turtle

def draw_heart():
    turtle.color("red")
    turtle.pensize(3)
    turtle.speed(3)
    
#    turtle.begin_fill()
    turtle.left(50)
    turtle.forward(100)
    turtle.circle(40, 180)
    turtle.right(100)
    turtle.circle(40, 180)
    turtle.forward(100)
#    turtle.end_fill()

def main():
    turtle.bgcolor("black")
    turtle.penup()
    turtle.goto(0, -50)
    turtle.pendown()
    draw_heart()
    turtle.hideturtle()
    turtle.done()

if __name__ == "__main__":
    main()
