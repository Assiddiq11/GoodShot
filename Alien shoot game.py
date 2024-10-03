import pgzrun
from random import randint

TITLE = "GOOD SHOT"

WIDTH = 500
HEIGHT = 500

message = ""

alien = Actor('alien')
alien.pos = 50,50

def draw():
    screen.clear()
    screen.fill('pink')
    screen.draw.text(message , center = (400,100),fontsize = 40)
    alien.draw()

def place_alien():
    alien.x = randint (50 , WIDTH-50)
    alien.y = randint (50 , WIDTH-50)

def mouse_down():
    global message
    if alien.collidepoint(pos):
        message = "You Hit The Alien!"
        place_alien()
    else:
        message = "You Missed!"

place_alien()
pgzrun.go()


