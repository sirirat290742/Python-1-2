import pgzrun
WIDTH = 800
HEIGHT = 400

def draw():
    global x1,y1
    screen.fill((0,255,255));
    screen.draw.text("shape2D_Animating",topleft=(250,10),fontsize=40,color="red")
    screen.draw.text("PYTHON",topleft=(x1,y1),fontsize=30,color="blue")



def update():
    global x1,y1
    x1 += 1
    if x1 > WIDTH :
        x1 = 0
    y1 += 1
    if y1 > HEIGHT :
        y1 = 0

x1 = int(WIDTH/2)
y1 = int(HEIGHT/2)
pgzrun.go()
