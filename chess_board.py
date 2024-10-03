from turtle import *

def draw_box(sides, colors, columns):
    """Draws a filled square with the given side length and color."""
    for column in range(columns):
        for color in colors:
            fillcolor(colors[column%2])
        begin_fill()
        for box in range(4):
            fd(sides)
            left(90)
        end_fill()
        fd(sides)
        end_fill()

def draw_board(sides, colors, columns, rows):
    """Draws a chessboard with the given parameters."""
    up()
    goto(-400,200)
    down()
    for row in range(rows):
        if (row%2)==0:
            draw_box(sides, colors, columns)
            right(180)
        if (row%2)==1:
            draw_box(sides, colors, columns)
            left(90)
            fd(2*sides) # Move to the next row
            left(90)    # Turn around for the next row
        
def main():
    """Sets up the turtle environment and draws the chessboard."""
    speed(0)
    tracer(1, 10)
    bgcolor("black")
    pensize(4)

    sides = 100
    columns = 8
    rows = 8
    colors = ["black", "white"]

    draw_board(sides, colors, columns, rows)
    up()
    goto(-400, 300)
    pd()
    pencolor("white"); hideturtle();
    write("CHESS  BOARD", font=("Arial",20,"bold"))
    for _ in range(4):
        fd(800)
        rt(90)

if __name__ == "__main__":
    main()
    mainloop()
