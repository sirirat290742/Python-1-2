import pgzrun
from random import randint

WIDTH = 800
HEIGHT = 600
Score = 0
Time = 0
Game_Over = False

fox = Actor('fox')
fox.pos = 100,100
coin = Actor('coin')
coin1 = Actor('coin1')
coin2 = Actor('coin2')

def draw():
    screen.fill('green')
    fox.draw()
    coin.draw()
    coin1.draw()
    coin2.draw()
    screen.draw.text('Score : '+str(Score),color='black',topleft=(10,10))
    screen.draw.text('Time : '+str(Time),color='black',topleft=(730,10))
    if Game_Over:
        screen.fill('pink')
        msg = "Time out, final score : " + str(Score)
        screen.draw.text(msg, topleft = (200,200), fontsize=50)
    
def place_coin():
    x = randint(30,WIDTH - 30)
    y = randint(30,HEIGHT - 30)
    coin.pos = (x,y)
    
def place_coin1():
    x = randint(40,WIDTH - 40)
    y = randint(40,HEIGHT - 40)
    coin1.pos = (x,y)

def place_coin2():
    x = randint(50,WIDTH - 50)
    y = randint(50,HEIGHT - 50)
    coin2.pos = (x,y)
    
def update():
    global Score
    if keyboard.left:
        fox.x = fox.x-2
    elif keyboard.right:
        fox.x = fox.x+2
    elif keyboard.up:
        fox.y = fox.y-2
    elif keyboard.down:
        fox.y = fox.y+2
    coin_collected = fox.colliderect(coin)
    if coin_collected:
        place_coin()
        Score += 1
    coin1_collected = fox.colliderect(coin1)
    if coin1_collected:
        place_coin1()
        Score += 1
    coin2_collected = fox.colliderect(coin2)
    if coin2_collected:
        place_coin2()
        Score += 1
def time_count():
    global Time
    Time += 1

def time_out():
    global Game_Over
    Game_Over = True

clock.schedule(time_out, 10.0)
clock.schedule_interval(time_count, 1.0)    
place_coin()
place_coin1()
place_coin2()
pgzrun.go()
