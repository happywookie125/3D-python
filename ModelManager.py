from settings import *

class Cube():
    def __init__(self, vertices, edges):
        self.vertices = vertices
        self.edges = edges
    
    def create(self):
        glBegin(GL_LINES)
        for edge in self.edges:
            for vertex in edge:
                glVertex3fv(self.vertices[vertex])
        glEnd()