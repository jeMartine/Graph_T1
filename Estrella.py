from hmac import new

import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import random, time

pygame.init()

screen_width = 1000
screen_height = 600
ortho_width = 100
ortho_height = 100

screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)
pygame.display.set_caption('Graphs in PyOpenGL')

def init_ortho():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, ortho_width, 0, ortho_height)
def star_algorithm(points):
    glBegin(GL_LINE_STRIP)
    for point in points:
        glVertex2f(point[0], point[1])
    glEnd()


done = False
init_ortho()
glPointSize(10000)
points = []
line = []
mouse_down = False

while not done:
    for event in pygame.event.get():
        if event.type == QUIT:
            done = True

    lines=[(1,2),(4,2),(1.5,0),(2.5,3.2), (3.5,0), (1,2)]

    n_stars=20
    constelation = []
    for _ in range(n_stars):
        new_star = []
        number1 = round(random.uniform(0, ortho_height), 2)
        number2 = round(random.uniform(0, ortho_height), 2)
        for line in lines:
            pos = (number1 + line[0], number2 + line[1])
            new_star.append(pos)

        constelation.append(new_star)


    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    for star in constelation:
        star_algorithm(star)
    pygame.display.flip()
    pygame.time.wait(10)
    time.sleep(1)
pygame.quit()
