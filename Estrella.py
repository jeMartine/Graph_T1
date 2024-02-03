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

def plot_point(center):
    glBegin(GL_POINTS)
    glVertex2f(center[0], center[1])
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

    n_stars=20
    constelation = []
    star_center = []
    for _ in range(n_stars):
        new_star = []
        #numeros aleatorios que dan cuanto me muevo en X y en Y
        number1 = round(random.uniform(0, ortho_height), 2)
        number2 = round(random.uniform(0, ortho_height), 2)
        #se crean nuevas coordenadas de una estrella para ponerse aleatoriamente en el plano
        for line in lines:
            pos = (number1 + line[0], number2 + line[1])
            #se crea una nueva estrella
            new_star.append(pos)

        #calcula el promedio de los puntos para encontrar el centro de la estrella
        x = round (sum(point[0] for point in new_star) / len(new_star), 2)
        y = round (sum(point[1] for point in new_star) / len(new_star), 2)
        aux = (x, y)
        star_center.append(aux)
        constelation.append(new_star)

    for cen in star_center:
        print(cen[0], cen[1])

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    #imprimir las estrellas
    for star in constelation:
        print_lines(star)

    #imprimir el centro de cada estrella
    print_lines(star_center)

    pygame.display.flip()
    pygame.time.wait(100000)
pygame.quit()
