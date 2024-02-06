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

    orion=[(0.63,4.69),(0.6,3.75),(0.41,3.66),(0.21,4.71),(0.41,3.66),(1.19,3.04),(1.73,2.82),(3.19,1,55),
          (3.5, 0.14),(5,1),(3.4,2.1),(3.32,1.79),(3.19,1,55),(3.32,1.79),(3.4,2.1), (3.17,3.4),
          (2.36,3.66),(1.73,2.82),(2.36,3.66),(3.17,3.4),(4.63,4.3),(4.39,4.6),(4.06,4.72),(4.39,4.6),
          (4.63,4.3),(4.72,4.03),(4.9,3.46),(4.86,3.19)]

    orion_b = [(val[0] * 15, val[1] * 18) for val in orion]


    constelation = []
    star_center = []
    for val in orion_b:
        new_star = []
        #numeros que indican cuanto me muevo en X y en Y
        number1 = (val[0]-2.5)
        number2 = (val[1]-1.5)
        #se crean nuevas coordenadas de una estrella para poner en el plano
        for line in lines:
            pos = (number1 + line[0], number2 + line[1])
            #se crea una nueva estrella
            new_star.append(pos)

        constelation.append(new_star)

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    #imprimir constelación
    print_lines(orion_b)

    #imprimir las estrellas
    for star in constelation:
        print_lines(star)

    pygame.display.flip()
    pygame.time.wait(10)
pygame.quit()
