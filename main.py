from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from rectangle import *

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 500
PERIOD = 10  # ms

playerScore = 0
pcScore = 0

deltaX = 1
deltaY = -1

FROM_RIGHT = 1
FROM_LEFT = 2
FROM_TOP = 3
FROM_BOTTOM = 4

mouse_x = 400

ball = rect(390, 240, 410, 260)
wall = rect(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT)
player = rect(0, 0, 80, 20)


def Init_Camera_Proj():
    glClearColor(0, 0, 0, 0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0, WINDOW_WIDTH, 0, WINDOW_HEIGHT, 0, 1)
    glMatrixMode(GL_MODELVIEW)
    # Let look at be it's default prameters
    glEnable(GL_DEPTH_TEST)


def display():
    global deltaX, deltaY, playerScore, pcScore
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glColor3f(1, 1, 1)
    draw_rect(ball)

    glPushMatrix()
    s1 = "PC : " + str(pcScore)
    draw_text(s1, 10, 460)
    glPopMatrix()

    glPushMatrix()
    s2 = "Player : " + str(playerScore)
    draw_text(s2, 10, 420)
    glPopMatrix()

    player.left = mouse_x - 30
    player.right = mouse_x + 30
    glColor3f(1, 1, 1)
    draw_rect(player)

    if test_plyer_ball(ball, player):
        deltaY = 1
        playerScore += 1

    # Collsion detection between Wall and Ball
    if test_wall_ball(ball, wall) == FROM_BOTTOM:
        deltaY = 1
        pcScore += 1
    if test_wall_ball(ball, wall) == FROM_LEFT:
        deltaX = 1
    if test_wall_ball(ball, wall) == FROM_RIGHT:
        deltaX = -1
    if test_wall_ball(ball, wall) == FROM_TOP:
        deltaY = -1

    ball.left += deltaX
    ball.right += deltaX
    ball.bottom += deltaY
    ball.top += deltaY

    glutSwapBuffers()


def test_wall_ball(ball: rect, wall: rect):
    if ball.right == wall.right:
        return FROM_RIGHT
    if ball.left == wall.left:
        return FROM_LEFT
    if ball.top == wall.top:
        return FROM_TOP
    if ball.bottom == wall.bottom:
        return FROM_BOTTOM
    return None


def test_plyer_ball(ball: rect, player: rect):
    if ball.bottom == player.top and ball.left >= player.left and ball.right <= player.right and deltaY == -1:
        return True
    if ball.bottom == player.top and ball.left < player.left and ball.right >= player.left and deltaY == -1:
        return True
    if ball.bottom == player.top and ball.right > player.right and ball.left <= player.right and deltaY == -1:
        return True
    return False


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


def mouse(x, y):
    """
    x,y : are the postion of mouse on window
    """
    global mouse_x
    mouse_x = x


def Timer(v):
    display()
    glutTimerFunc(PERIOD, Timer, 1)


if __name__ == "__main__":
    glutInit()
    glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)
    glutInitWindowPosition(50, 50)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH)
    glutCreateWindow("Ball Bat")
    glutDisplayFunc(display)
    glutTimerFunc(PERIOD, Timer, 1)
    glutKeyboardFunc(keyboard)
    glutPassiveMotionFunc(mouse)
    Init_Camera_Proj()
    glutMainLoop()
