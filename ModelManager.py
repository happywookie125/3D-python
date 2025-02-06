from settings import *

class Cube():
    def __init__(self, vertices, edges, surfaces, colors):
        self.vertices = vertices #points in 3D space
        self.edges = edges #A line connecting 2 vertices together
        self.surfaces = surfaces #A Collection of 4 vertices connected by a plane
        self.colors = colors #colors
    
    def create(self):
        glBegin(GL_QUADS)
        for surface in self.surfaces:
            x = 0
            for vertex in surface:
                x += 1
                glColor3fv(self.colors[x])
                glVertex3fv(self.vertices[vertex])
        glEnd()
        
        glBegin(GL_LINES)
        for edge in self.edges:
            for vertex in edge:
                glVertex3fv(self.vertices[vertex])
        glEnd()

        