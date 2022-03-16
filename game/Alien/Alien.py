import pgzrun
import time

WIDTH = 800
HEIGHT = 600
alien = Actor('alien')

def draw():
    screen.fill( (210,0,0) )
    alien.draw()

def update():
    alien.left += 2
    if alien.left > WIDTH:
       alien.right = 0

def on_mouse_down(pos, button):
    if button == mouse.LEFT and alien.collidepoint(pos):
        print('Eek')
        sound.eep.play()
    else :
        print('you missed')

def on_mouse_down(pos, button):
    if button == mouse.LEFT and alien.collidepoint(pos):
        sound.eep.play()
        alien.image = 'alien_hurt'
        time.sleep(1)
        alien.image = 'alien'
    else :
        print('you missed')


pgzrun.go()
