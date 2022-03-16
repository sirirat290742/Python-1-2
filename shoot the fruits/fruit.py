import pgzrun
import random
WIDTH = 900
HEIGHT = 600
apple = Actor ("apple")

def draw():
    screen.fill ( (100,200,200) )
    apple.draw()
   
def place_apple():
    apple.x = random.randint(40 , 600)
    apple.y = random.randint(40 , 400)

def on_mouse_down(pos):
    if apple.collidepoint(pos):
        print("Good chot!")
        place_apple()
    else:
        print("You Missed")
place_apple()
pgzrun.go()

