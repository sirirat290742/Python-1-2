# Example 10-1
import pgzrun
from random import randint

#Function for display
def draw() :
    screen.blit('bg1' , (0,0))
    for alien in aliens :
        alien.draw()

def update() :
    for alien in aliens:
        alien.x += 1
        alien.y += 1
        if alien.top > HEIGHT :
            alien.bottom = 0
        if alien.left > WIDTH :
            alien.right = 0

def on_mouse_down(pos) :
    for alien in aliens :
        if alien.collidepoint(pos):
            aliens.remove(alien)


def create_alien() :
    global Num
    aliens.append(Actor('alien'))
    last = len(aliens)
    aliens[last - 1].x = randint(50 , WIDTH - 50)
    aliens[last - 1].y = randint(50 , HEIGHT - 50)
    Num += 1

#main
#define size windows
WIDTH = 1000
HEIGHT = 600

#create object
Num = 0
aliens = [ ]
clock.schedule_interval(create_alien , 0.5)

#Example 10-2
import pgzrun
from random import randint

#Function for display
def draw() :
    screen.blit('backdrop800' , (0,0))
    ship.draw()
    alien.draw()
    for bullet in bullets :
        bullet.draw()
    screen.draw.text("Bullet : " +str(len(bullets)), topleft = (10 , 10) , fontsize = 28 , color = 'white')

def on_key_down(key) :
    if key == keys.SPACE :
        bullets.append(Actor('bullet'))
        last = len(bullets)
        bullets[last - 1].pos = ship.pos


def update() :
    # check key for move ship
    if keyboard.LEFT :
        ship.x -= 1
        if ship.left < 0 :
            ship.left = 0
    elif keyboard.RIGHT :
        ship.x += 1
        if ship.right > WIDTH :
                ship.ridht = WIDTH
   # move bullet
    for bullet in bullets :
       bullet.y -= 2
       if bullet.top < 0 :
           bullets. remove(bullet)

   # move alien
    alien.left += 2
    if alien.left > WIDTH :
        alien.right = 0
    # collision
    for bullet in bullets :
        if bullet.y < 100 :
           if bullet.colliderect(alien) :
              alien.pos = (60 , 30)
              bullets.remove( bullet)
           

# main
# define size
WIDTH = 800
HEIGHT = 600

#create
ship = Actor('ship')
ship.pos = (WIDTH / 2 , HEIGHT - 40)
bullets = [ ]
alien = Actor('alien')
alien.pos = (400 , 50)
pgzrun.go()


