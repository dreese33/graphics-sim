""" Common line and camera focuses """
import vpython as vp


def create_origin_line():
    """
    Line with first point, beginning at the origin of the graph
    """
    moving_line = vp.curve()
    moving_line.append(
        vp.vector(0, 0, 0),
    )

    return moving_line
