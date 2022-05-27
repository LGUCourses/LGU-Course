import turtle
import random
from turtle import *

# ---------- constant variables ----------
# board_size = 5
rect_size = 60
white_space = 6
figure_size = 4
bar_x = -0.5                                                  # translation parameter of bar_x
bar_y = -3.5                                                  # translation parameter of bar_y
col_tb = ['red', 'yellow', 'blue', 'purple', 'lightcoral']    # table of color id 
# ----------- global variables -----------
g_board, g_bar, g_ink = None, None, None                      # brush of board, color bar, ink
g_s = None                                                    # screen control
g_status = 0                                                  # mouse status : [ choose / flip ]
g_srect = None                                                # selected rectangle
g_col = []                                                    # random board color
# ----------------------------------------


def put_rectangle(t, x, y, col):
    # generate the rectangle element.
    pos_x = x*(white_space+rect_size)
    pos_y = y*(white_space+rect_size) # transform rectangle index to exact position

    # config (position & color) of brush
    t.pu()
    t.pensize(0)
    t.goto(pos_x-rect_size//2, pos_y-rect_size//2)
    t.color(col_tb[col])
    t.pd()

    # fill the (x, y) rectangle with color
    t.begin_fill()
    for i in range(4):
        t.fd(rect_size)
        t.left(90)
    t.end_fill()


def rectangle_inking(t, x, y, col='indigo'):
    # draw figure of rectangle element.
    pos_x = x*(white_space+rect_size)
    pos_y = y*(white_space+rect_size) # transform rectangle index to exact position

    # config (position & color & pensize) of brush
    t.pu()
    t.goto(pos_x-rect_size//2, pos_y-rect_size//2-figure_size//2)
    t.color(col)
    t.pensize(figure_size)
    t.pd()

    # show the line track around the (x, y) rectangle
    for i in range(4):
        t.fd(rect_size+figure_size//2)
        t.left(90)


def generate_board():
    # generate the main square board.
    for x in range(-2, 3):
        for y in range(-2, 3):
            put_rectangle(g_board, x, y, g_col[x+2][y+2])


def generate_color_bar():
    # generate the select color bar
    for x in range(-2, 3):
        put_rectangle(g_bar, x+bar_x, -3.5, x+2)
        rectangle_inking(g_bar, x+bar_x, -3.5, 'black')
        # translation x -= 0.5, y = -3.5


def flipping(rect, col, t_col):
    x, y = rect
    if abs(x) > 2 or abs(y) > 2:      # out of range
        return
    if g_col[x+2][y+2] != col:        # not a feasible rectangle
        return
    
    g_col[x+2][y+2] = t_col
    flipping((x+1, y), col, t_col)
    flipping((x-1, y), col, t_col)
    flipping((x, y+1), col, t_col)
    flipping((x, y-1), col, t_col)    # flip neighbor block


def select_rectangle(cli_x, cli_y): 
    # denote the position of click point as (cli_x, cli_y)
    # judge the current mode : [ select / flip ]
    global g_status, g_srect

    # mode 1: select rectangle
    for x in range(-2, 3):
        for y in range(-2, 3):
            pos_x = x*(white_space+rect_size)
            pos_y = y*(white_space+rect_size)
            if abs(cli_x-pos_x) <= rect_size//2 and abs(cli_y-pos_y) <= rect_size//2:
                # find which rectangle the point is located in.
                g_status = 1
                g_srect = (x, y)
                g_ink.clear()
                rectangle_inking(g_ink, x, y)
                g_s.update()
                return

    # mode 2: color clip
    if g_status == 1:
        for x in range(-2, 3):
            pos_x = (x+bar_x)*(white_space+rect_size)
            pos_y = (-3.5)*(white_space+rect_size)
            if abs(cli_x-pos_x) <= rect_size//2 and abs(cli_y-pos_y) <= rect_size//2:
                # find which rectangle the point is located in.
                g_status = 0
                g_ink.clear()
                if x+2 != g_col[g_srect[0]+2][g_srect[1]+2]:
                    flipping(g_srect, g_col[g_srect[0]+2][g_srect[1]+2], x+2)
                    # repaint the board
                    g_board.clear()
                    generate_board()
                    g_s.update()
                return


if __name__ == "__main__":
    # config of turtle module
    title('Color Flipping')
    text = Turtle()
    text.ht()
    text.pu()
    text.goto(-270, 200)
    text.write('''
    This is a game called Color Flip, where you can have different colors
    for 5x5 blocks. After the game starts, you can choose a block in the
    square board and choose a color from the color bar below. All blocks
    connected with the same color will become the color you choose.
    Your goal is to turn the entire square board into one color.
    ''', move='True', align='left', font=('Arial', 16, 'normal'))
    g_board = Turtle()
    g_bar = Turtle()
    g_ink = Turtle()
    g_board.ht()
    g_bar.ht()
    g_ink.ht()
    g_s = Screen()
    g_s.delay(0)
    
    # generate random board color
    g_col = [[random.randint(0, 4) for _ in range(5)] for _ in range(5)]
    generate_board()
    generate_color_bar()
    
    # graphic user interface
    g_s.tracer(0)
    g_s.onclick(select_rectangle)
    g_s.mainloop()
