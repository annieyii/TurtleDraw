import turtle

def draw_star(size):
    turtle.color("gold")
    for _ in range(5):
        turtle.forward(size)
        turtle.right(144)
def main():
    turtle.bgcolor("black")
    turtle.speed(3)
    turtle.penup()
    turtle.goto(-50, 0)
    turtle.pendown()
    draw_star(100)
    turtle.hideturtle()
    turtle.done()

if __name__ == "__main__":
    main()
