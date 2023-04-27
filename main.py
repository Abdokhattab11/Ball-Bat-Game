from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from rectangle import *

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 500
PERIOD = 10  # ms

PLAYER_CNT = 0
PC_CNT = 0

ball = rect(400, 250, 420, 270)
window = rect(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT)
player = rect(0, 0, 80, 20)


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
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glColor3f(1, 1, 1)
    draw_rect(ball)
    draw_rect(player)

    glPushMatrix()
    s1 = "PC : " + str(PC_CNT)
    draw_text(s1, 10, 460)
    glPopMatrix()

    glPushMatrix()
    s2 = "Player : " + str(PLAYER_CNT)
    draw_text(s2, 10, 420)
    glPopMatrix()

    glutSwapBuffers()


def draw_text(string, x, y):
    """
    string : is the str to be drawn
    x , y : are shift 
    """
    glColor3f(1, 1, 0)
    glLineWidth(2)
    glTranslate(x, y, 0)
    glScale(0.15, 0.15, 0.15)
    string = string.encode()
    for char in string:
        glutStrokeCharacter(GLUT_STROKE_ROMAN, char)


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
    Init_Camera_Proj()
    glutMainLoop()
