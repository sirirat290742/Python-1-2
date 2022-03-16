import pgzrun
import random
WIDTH = 900
HEIGHT = 600
apple = Actor ("apple")
orange = Actor ("orange")
pineapple = Actor ("pineapple")

def draw():
    screen.fill ( (100,200,200) )
    apple.draw()
    orange.draw()
    pineapple.draw()
   
def place_apple():
    apple.x = random.randint(40 , 600)
    apple.y = random.randint(40 , 400)
    
def place_orange():
    orange.x = random.randint(30 , 600)
    orange.y = random.randint(30 , 400)

def place_pineapple():
    pineapple.x = random.randint(20 , 600)
    pineapple.y = random.randint(20 , 400)


def on_mouse_down(pos):
    if apple.collidepoint(pos):
        print("Good chot!")
        place_apple()
    else:
        print("You Missed")

def on_mouse_up(pos):
    if orange.collidepoint(pos):
        print("Good chot!")
        place_orange()
    else:
        print("You Missed")

def on_mouse_down(pos):
    if pineapple.collidepoint(pos):
        print("Good chot!")
        place_pineapple()
    else:
        print("You Missed")
place_apple()
place_orange()
place_pineapple()
pgzrun.go()

