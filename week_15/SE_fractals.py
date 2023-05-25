import turtle


def draw_fractal_side(t, length, level):

    if level == 0:
        t.forward(length)
        return

    length /= 3.0
    draw_fractal_side(t, length, level - 1)
    t.left(60)
    draw_fractal_side(t, length, level - 1)
    t.right(120)
    draw_fractal_side(t, length, level - 1)
    t.left(60)
    draw_fractal_side(t, length, level - 1)


def draw_fractal_square(length, level):
    t = turtle.Turtle()
    for _ in range(4):
        draw_fractal_side(t, length, level)
        t.right(90)

    turtle.done()


draw_fractal_square(300, 3)
