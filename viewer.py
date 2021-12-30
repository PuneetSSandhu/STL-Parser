import pygame
from pygame.locals import *
import sys
from OpenGL.GL import *
from OpenGL.GLU import *
from stlParser import *


def draw_stl(file_name):
    faces = parse_stl(file_name)
    for face in faces:
        glBegin(GL_POLYGON)
        glNormal3f(face.normal.x, face.normal.y, face.normal.z)
        for vertex in face.vertices:
            glVertex3f(vertex.x, vertex.y, vertex.z)
        glEnd()

def main():
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    glTranslatef(0.0,0.0, -5)

    glRotatef(0, 0, 0, 0)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        draw_stl(sys.argv[1])
        pygame.display.update()
        pygame.time.wait(10)



if __name__ == '__main__':
    # take command line argument
    if len(sys.argv) != 2:
        print("Usage: python3 viewer.py <file_name>")
        exit(1)
    main()
    print("Done!")
