from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import rectangle

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 500
PERIOD = 10  # ms


def Init_Camera_Proj():
    glClearColor(0, 0, 0, 0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0, WINDOW_WIDTH, 0, WINDOW_HEIGHT, 0, 1)
    glMatrixMode(GL_MODELVIEW)
    # Let look at be it's default prameters
    glEnable(GL_DEPTH_TEST)


def Timer(v):
    display()
    glutTimerFunc(PERIOD, Timer, 1)


def display():
    glutSwapBuffers()


def keyboard(key, x, y):
    """
    key : hitted key on keyboard 
    x : x postion of mouse on window
    y : y postion of mouse on window
    """
    if key == b"q":
        sys.exit(0)


if __name__ == "__main__":
    glutInit()
    glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)
    glutInitWindowPosition(50, 50)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH)
    glutCreateWindow("Ball Bat")
    glutDisplayFunc(display)
    glutTimerFunc(PERIOD, Timer, 1)
    glutKeyboardFunc(keyboard)
    glutMainLoop()
