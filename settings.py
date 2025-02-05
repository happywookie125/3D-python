from pygame import *
from OpenGL.GL import *
from OpenGL.GLU import *
import ModelManager as Model
import numpy as np
import sys
import OpenGL

class Help:
    def __init__(self):
        self.clock = time.Clock()

    def getFramesAsString(self) -> str:
        return str(int(time.Clock.get_fps(self.clock)))
        