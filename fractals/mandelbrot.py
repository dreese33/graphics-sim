""" Drawing fractals w/ animations """
import vpython as vp
from common_shapes import lines


def draw_mandelbrot_animation(C, total_pts = 10):
    """
    TODO Incomplete
    Mandelbrot set can be generated via:
    Z_{n+1} = Z_{n}^2 + C
    """
    z_n = 0
    moving_line = lines.create_origin_line()

    for t in range(0, total_pts):
        vp.rate(5)
        z_n = z_n*z_n + C
        moving_line.append(
            vp.vector(t, z_n, 0)
        )
