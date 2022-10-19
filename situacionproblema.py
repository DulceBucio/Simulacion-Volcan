from pygame import *
import sys
import math

def coord(ang, vinicial):
    ang1 = math.radians(ang)
    x1 = 0 
    ycoord = []
    xcoord = []

    while x1 < 1000:
        y1 = (x1*math.tan(ang1))-((9.8*x1*x1))/(2*(vinicial*vinicial)*(math.cos(ang1)*math.cos(ang1)))
        x1 = x1 + 50
        ycoord.append(y1)
        xcoord.append(x1)

    return xcoord, ycoord

def anim(xcoord, ycoord):
    puntos = 0
    while puntos < len(xcoord):
        draw.rect(screen, (255,0,0), (xcoord[puntos], 300-ycoord[puntos], 10,10), 3)
        puntos += 1

def criticos(ang,vinicial):
    ang1 = math.radians(ang)
    alcance = ((vinicial*vinicial)*math.sin(2*ang1))/9.81
    alturamax = (2*vinicial*math.sin(ang1))/(2*9.81)

    return alcance, alturamax


init()
screen = display.set_mode((800,600))
animar = False
clock = time.Clock()
calibri = font.SysFont('Calibri', 10)

while True:
    screen.fill((255,255,255))
    for e in event.get():
        if e.type == QUIT: sys.exit()
        clock.tick(15)
        if e.type == KEYDOWN and e.key == K_1:
            animar = True
    
    leyenda1 = calibri.render("Trayectoria actual: ", True, (0,0,0))
    screen.blit(leyenda1, (0,0))
    if animar: 
        x1, y2 = coord(30,100)
        anim(x1, y2)
    
    display.flip()