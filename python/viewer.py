import pygame
from pygame.locals import *
import sys
from OpenGL.GL import *
from OpenGL.GLU import *
from stlParser import *
import numpy as np

colors = []


def draw_stl(file_name):
    faces = extract_faces(file_name)

    for face, color in zip(faces, colors):
        glBegin(GL_POLYGON)
        glNormal3f(face.normal.x, face.normal.y, face.normal.z)
        for vertex in face.vertices():
            glVertex3f(vertex[0], vertex[1], vertex[2])
            #make the face a random shade of red
            glColor3f(color[0], color[1], color[2])
        glEnd()


def main():
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    glMatrixMode(GL_PROJECTION)
    gluPerspective(90, (display[0]/display[1]), 0.1, 500.0)

    glMatrixMode(GL_MODELVIEW)
    glTranslatef(0, 0, -100)
    glRotatef(0, 0, 0, 0)

    glLight(GL_LIGHT0, GL_POSITION,  (0, 0, 1, 0)) # directional light from the front
    # glLight(GL_LIGHT0, GL_POSITION,  (5, 5, 5, 1)) # point light from the left, top, front
    glLightfv(GL_LIGHT0, GL_AMBIENT, (0, 0, 0, 1))
    glLightfv(GL_LIGHT0, GL_DIFFUSE, (1, 1, 1, 1))


    #generate random colors for the faces
    faces = extract_faces(sys.argv[1])
    if not faces:
        pygame.quit()
        quit()

    for i in range(len(faces)):
            colors.append((1,1,255-255*i/len(faces), 1))

    while True:
        # draw the x,y,z axes
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    glRotatef(1, 0, 1, 0)
                if event.key == pygame.K_RIGHT:
                    glRotatef(-1, 0, 1, 0)
                if event.key == pygame.K_UP:
                    glRotatef(1, 1, 0, 0)
                if event.key == pygame.K_DOWN:
                    glRotatef(-1, 1, 0, 0)
                # zoom out
                if event.key == pygame.K_z:
                    glTranslatef(0,0,1)
                # zoom in
                if event.key == pygame.K_x:
                    glTranslatef(0,0,-1)

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)


        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)
        glEnable(GL_COLOR_MATERIAL)
        glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE )

        draw_stl(sys.argv[1])

        glDisable(GL_LIGHT0)
        glDisable(GL_LIGHTING)
        glDisable(GL_COLOR_MATERIAL)
        pygame.display.flip()
        pygame.time.wait(10)



if __name__ == '__main__':
    # take command line argument
    if len(sys.argv) != 2:
        print("Usage: python3 viewer.py <file_name>")
        exit(1)
    main()
    print("Done!")
