from hmac import new

import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

pygame.init()

screen_width = 1000
screen_height = 600
ortho_width = 5
ortho_height = 5

screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)
pygame.display.set_caption('Graphs in PyOpenGL')

def init_ortho():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, ortho_width, 0, ortho_height)

def print_lines(points):
    glBegin(GL_LINE_STRIP)
    for point in points:
        glVertex2f(point[0], point[1])
    glEnd()


done = False
init_ortho()
glPointSize(5)
points = []
line = []
mouse_down = False

while not done:
    for event in pygame.event.get():
        if event.type == QUIT:
            done = True
    #puntos para crear una estrella
    lines=[(1,2),(4,2),(1.5,0),(2.5,3.2), (3.5,0), (1,2)]

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    #imprimir la estrella

    print_lines(lines)

    pygame.display.flip()
    pygame.time.wait(10)
pygame.quit()
