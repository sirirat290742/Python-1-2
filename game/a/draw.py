WIDTH = 800
HIGHT = 600
fox  =Actor ('fox')
fox.pos = 100.100
coin = Actor ('coin')
def draw():
    screen.fill('green')
    fox.draw()
    coin.draw()

place_coin()
pgzrun.go()                                                                                       
