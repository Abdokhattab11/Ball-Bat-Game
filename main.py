from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from rectangle import *

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 500
PERIOD = 10  # ms

player2Score = 0
player1Score = 0

deltaX = 1
deltaY = -1

FROM_RIGHT = 1
FROM_LEFT = 2
FROM_TOP = 3
FROM_BOTTOM = 4

mouse_x = 400
keyboard_x = 400

ball = rect(390, 240, 410, 260)
wall = rect(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT)
player1 = rect(0, 0, 80, 20)
player2 = rect(0, 480, 80, 500)

curr_color = 1


def Init_Camera_Proj():
    glClearColor(0, 0, 0, 0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0, WINDOW_WIDTH, 0, WINDOW_HEIGHT, 0, 1)
    glMatrixMode(GL_MODELVIEW)
    # Let look at be it's default prameters
    glEnable(GL_DEPTH_TEST)


def display():
    global deltaX, deltaY, player2Score, player1Score, curr_color
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glPushMatrix()
    s1 = "Player1 : " + str(player1Score)
    draw_text(s1, 10, 460)
    glPopMatrix()

    glPushMatrix()
    s2 = "Player2 : " + str(player2Score)
    draw_text(s2, 10, 420)
    glPopMatrix()

    glColor3f(1, curr_color, curr_color)
    draw_rect(ball)
    player1.left = mouse_x - 40
    player1.right = mouse_x + 40
    draw_rect(player1)

    if test_player1_ball(ball, player1):
        curr_color = 0
        deltaY = 1
        player1Score += 1

    if test_player2_ball(ball, player2):
        curr_color = 0
        deltaY = -1
        player2Score += 1

    # Collsion detection between Wall and Ball
    if test_wall_ball(ball, wall) == FROM_BOTTOM:
        deltaY = 1
        player1Score += 1
    if test_wall_ball(ball, wall) == FROM_LEFT:
        deltaX = 1
    if test_wall_ball(ball, wall) == FROM_RIGHT:
        deltaX = -1
    if test_wall_ball(ball, wall) == FROM_TOP:
        deltaY = -1

    player2.left = keyboard_x - 40
    player2.right = keyboard_x + 40
    draw_rect(player2)
    print(keyboard_x)

    ball.left += deltaX
    ball.right += deltaX
    ball.bottom += deltaY
    ball.top += deltaY
    if curr_color < 1:
        curr_color += 0.01
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


def test_player1_ball(ball: rect, player: rect):
    if ball.bottom == player.top and ball.left >= player.left and ball.right <= player.right and deltaY == -1:
        return True
    if ball.bottom == player.top and ball.left < player.left and ball.right >= player.left and deltaY == -1:
        return True
    if ball.bottom == player.top and ball.right > player.right and ball.left <= player.right and deltaY == -1:
        return True
    return False


def test_player2_ball(ball: rect, player: rect):
    if ball.top == player.bottom and ball.left >= player.left and ball.right <= player.right and deltaY == 1:
        return True
    if ball.top == player.bottom and ball.left < player.left and ball.right >= player.left and deltaY == 1:
        return True
    if ball.top == player.bottom and ball.right > player.right and ball.left <= player.right and deltaY == 1:
        return True
    return False


def draw_text(string, x, y):
    glColor3f(1, 1, 0)
    glLineWidth(2)
    glTranslate(x, y, 0)
    glScale(0.15, 0.15, 0.15)
    string = string.encode()
    for char in string:
        glutStrokeCharacter(GLUT_STROKE_ROMAN, char)


def keyboard(key, x, y):
    global keyboard_x
    if key == b"a":
        keyboard_x = max(0, keyboard_x - 10)
    if key == b"d":
        keyboard_x = min(keyboard_x + 10, WINDOW_WIDTH)
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
