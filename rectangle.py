from OpenGL.GL import *


class rect:
    def __init__(self, left, bottom, right, top):
        self.left = left
        self.bottom = bottom
        self.right = right
        self.top = top


def draw_rect(r: rect):
    glBegin(GL_POLYGON)
    glVertex(r.left, r.bottom, 0)
    glVertex(r.right, r.bottom, 0)
    glVertex(r.right, r.top, 0)
    glVertex(r.left, r.top, 0)
    glEnd()


if __name__ == "__main__":
    print("Hello World")
