import turtle

screen = turtle.Screen()


def screen_define():
    #screen definition
    screen.setup(width=800, height=600)
    screen.bgcolor("white")
    screen.title("Tic Tac Toe")




def make_board():
    size = int(screen.numinput("choose size", "enter the size of the board", default=3, minval=3, maxval=10))
    #board making
    board_size = 450
    cell_size = board_size / size
    x = -board_size / 2
    y = board_size / 2

    pen = turtle.Turtle()
    pen.hideturtle()
    pen.speed(0)
    pen.pensize(4)

    screen.tracer(0)
    for i in range(size + 1):
        #horizontal line
        pen.penup()
        pen.goto(x, y - i * cell_size)
        pen.pendown()
        pen.goto(x + board_size, y - i * cell_size)
        #vertical line
        pen.penup()
        pen.goto(x + i * cell_size, y)
        pen.pendown()
        pen.goto(x + i * cell_size, y - board_size)
    screen.update()

screen_define()
make_board()
turtle.mainloop()
