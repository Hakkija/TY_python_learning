import turtle


def draw_fractal(x_start, y_start, x_end, y_end, vertical=True):
    # base case: stop when the width or height is 1 pixel
    if abs(x_end - x_start) <= 1 or abs(y_end - y_start) <= 1:
        return
    else:
        if vertical:
            mid_x = (x_start + x_end) / 2

            # draw a vertical line to divide the window
            turtle.penup()
            turtle.goto(mid_x, y_start)
            turtle.pendown()
            turtle.goto(mid_x, y_end)

            # recursively divide the right and left halves of the window
            draw_fractal(mid_x, y_start, x_end, y_end, not vertical)
            draw_fractal(x_start, y_start, mid_x, y_end, not vertical)
        else:
            mid_y = (y_start + y_end) / 2

            # draw a horizontal line to divide the window
            turtle.penup()
            turtle.goto(x_start, mid_y)
            turtle.pendown()
            turtle.goto(x_end, mid_y)

            # recursively divide the top and bottom halves of the window
            draw_fractal(x_start, mid_y, x_end, y_end, not vertical)
            draw_fractal(x_start, y_start, x_end, mid_y, not vertical)


# Set up the window size
turtle.setup(600, 400)

# Set the speed and shape of the turtle
turtle.speed(0)
turtle.shape("turtle")

# Draw the fractal
draw_fractal(-300, 200, 300, -200)

# Hide the turtle and keep the window open
turtle.hideturtle()
turtle.done()
