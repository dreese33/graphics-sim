""" Animations involving polynomials """
import vpython as vp
# import numpy as np

def create_origin_line():
    """
    Line with first point, beginning at the origin of the graph
    """
    moving_line = vp.curve()
    moving_line.append(
        vp.vector(0, 0, 0),
    )

    return moving_line


def draw_parabola_animation(a, b, c, total_pts = 5):
    """
    Equation for a parabola:
    y = ax^2 + bx + c
    """
    moving_line = create_origin_line()

    for x in range(0, total_pts):
        vp.rate(5)
        y = a*x*x + b*x + c
        moving_line.append(
            vp.vector(x, y, 0)
        )


# def draw_mandelbrot_animation(C, totalPts = 10):
#   """
#   Mandelbrot set can be generated via:
#   Z_{n+1} = Z_{n}^2 + C
#   """
#   z_n = 0
#   moving_line = create_origin_line()

#   for t in range(0, totalPts):
#     rate(5)
#     z_n = z_n*z_n + C
#     moving_line.append(
#       vector(t, z_n, 0)
#     )

draw_parabola_animation(1, -2, 0, 20)
# draw_mandelbrot_animation(2)
