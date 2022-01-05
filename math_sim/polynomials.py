""" Animations involving polynomials """
import vpython as vp
from common_shapes import lines


def draw_parabola_animation(a, b, c, total_pts = 5):
    """
    Equation for a parabola:
    y = ax^2 + bx + c
    """
    moving_line = lines.create_origin_line()

    for x in range(0, total_pts):
        vp.rate(5)

        y = a*x*x + b*x + c
        vp.scene.camera.axis = vp.vector(0, 0, -y*2)
        vp.scene.camera.pos = vp.vector(0, 0, y*2)

        moving_line.append(
            vp.vector(x, y, 0)
        )


draw_parabola_animation(1, 0, 0, 20)
