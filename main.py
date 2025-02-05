from settings import *
import pygame

pygame.init()

#window class
class Window:
    def __init__(self, name : str, bg_color : Vector3, size : Vector2):
      self.name = name
      self.bg_color = bg_color
      self.size = size

    def update(self):
       pass
    
    def quit(self):
       pygame.quit()
       pygame.display.quit()
       exit()

size = Vector2(300,300)
bg_color = Vector3(0,0,0)

window = Window("test", bg_color, size)
running = True
keys = key.get_pressed()

#setup window
screen = display.set_mode(window.size) #create window variable
display.set_caption(window.name) #set window title
screen.fill(window.bg_color) #set window color
display.flip() #update display


while running:
   keys = key.get_pressed()
   window.update()
   

   for event in pygame.event.get():
        if keys[K_ESCAPE]:
           window.quit()
      
        # Check for QUIT event       
        if event.type == pygame.QUIT: 
            running = False
