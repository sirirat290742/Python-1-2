import pgzrun
import time
WIDTH = 800
HEIGHT = 600
alien = Actor('alien')
alien.pos = 0, 70
alien2 = Actor('alien')
alien2.pos = 0,290
alien3 = Actor('alien')
alien3.pos = 0,500
def draw():
    screen.fill((210,0,0))
    alien.draw()
    alien2.draw()
    alien3.draw()
def update():
    alien3.left +=3
    alien2.left +=5
    alien.left  +=2
    if alien.left > WIDTH:
        alien.right=0
    if alien2.left > WIDTH:
        alien2.right = 0
    if alien3.left > WIDTH:
        alien3.right = 0
def on_mouse_down(pos,button):
    if button == mouse.LEFT and alien.collidepoint(pos):
        set_alien_hurt()
    elif button == mouse.LEFT and alien2.collidepoint(pos):
        set_alien_hurt2()
    elif button == mouse.LEFT and alien3.collidepoint(pos):
        set_alien_hurt3()
def set_alien_hurt():
    alien.image = 'alien_hurt'
    sounds.eep.play()
    clock.schedule(set_alien_normal,0.1)
def set_alien_normal():
    alien.image = 'alien'
def set_alien_hurt2():
    alien2.image = 'alien_hurt'
    sounds.eep.play()
    clock.schedule(set_alien_normal2,0.1)
def set_alien_normal2():
    alien2.image = 'alien'
def set_alien_hurt3():
    alien3.image = 'alien_hurt'
    sounds.eep.play()
    clock.schedule(set_alien_normal3,0.1)
def set_alien_normal3():
    alien3.image = 'alien'
pgzrun.go()
