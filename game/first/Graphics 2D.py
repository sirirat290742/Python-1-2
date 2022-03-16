import pgzrun
WIDTH = 640
HEIGHT = 480

def draw():
    screen.fill((255,255,255));
    screen.draw.text("show graphics 2d",topright=(600,10),fontsize=30,color="blue")
    screen.draw.line( (40,20),(600,460),(255,0,0) )
    screen.draw.filled_circle( (450,180),80,"yellow" )
    screen.draw.circle( (450,180), 80, "red" )
    screen.draw.filled_rect( Rect ((80,280),(150,100)),"green" )
    screen.draw.rect( Rect ((80,280),(150,100)), "magenta")
pgzrun.go()
