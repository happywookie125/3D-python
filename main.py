from settings import *
import pygame

pygame.init()

#window class
class Window:
    def __init__(self, name : str, bg_color : Vector3, size : Vector2):
      self.name = name
      self.bg_color = bg_color
      self.size = size
      print("Testing Engine")

    def update(self):
       pass

    
    def quit(self):
       pygame.quit()
       pygame.display.quit()
       sys.exit()

size = Vector2(800,800)
bg_color = Vector3(0,0,0)

window = Window("test", bg_color, size)
running = True
keys = key.get_pressed()

#cube variables
vertices = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
)

edges = (
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,7),
    (6,3),
    (6,4),
    (6,7),
    (5,1),
    (5,4),
    (5,7)
)

colors = (
    (1,0,0),
    (0,1,0),
    (0,0,1),
    (0,1,0),
    (1,1,1),
    (0,1,1),
    (1,0,0),
    (0,1,0),
    (0,0,1),
    (1,0,0),
    (1,1,1),
    (0,1,1),
)

surfaces = (
   (0,1,2,3),
    (3,2,7,6),
    (6,7,5,4),
    (4,5,1,0),
    (1,5,7,2),
    (4,0,3,6)
)

model = Model.Cube(vertices, edges, surfaces, colors)
help = Help()

#setup window
screen = display.set_mode(window.size, DOUBLEBUF|OPENGL) #create window variable
display.set_caption(window.name) #set window title
screen.fill(window.bg_color) #set window color
display.flip() #update display

#setup camera
gluPerspective(45, (size[0]/size[1]), 0.1, 50.0)

#setup cube
glTranslatef(0,0,-5)


while running:
   keys = key.get_pressed()
   window.update()

   #rotate cube
   glRotatef(1,3,1,1)
   glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
   model.create()
   display.flip()
   time.wait(10)

   for event in pygame.event.get():
        if keys[K_ESCAPE]:
           window.quit()
      
        # Check for QUIT event       
        if event.type == pygame.QUIT: 
            running = False
