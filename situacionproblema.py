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

def resistencia(ang, vinicial, t):
    ang1 = math.radians(ang)
    vox = vinicial*math.cos(ang1)
    voy =  vinicial*math.sin(ang1)
    av = vinicial/2
    xcoordr = []
    ycoordr = []
    while t < 1000:
        y1 = vox*t + ((av*t*t)/2)
        yr = voy*t + ((-9.81*t*t)/2)
        t = t + 1
        ycoordr.append(y1)
        xcoordr.append(x1)
    return xcoordr, ycoordr


def anim(xcoordr, ycoordr):
    puntos = 0
    while puntos < len(xcoordr):
        draw.rect(screen, (255,0,0), (xcoordr[puntos], 300-ycoordr[puntos], 10,10), 3)
        time.delay(300)
        display.update()
        puntos += 1

def animr(xcoordr, ycoordr):
    puntos = 0
    while puntos < len(xcoordr):
        draw.rect(screen, (0,255,0), (xcoordr[puntos], 300-ycoordr[puntos], 10, 10), 3)
        time.delay(300)
        display.update()
        puntos += 1

def criticos(ang,vinicial):
    ang1 = math.radians(ang)
    alcance = ((vinicial*vinicial)*math.sin(2*ang1))/9.81
    alturamax = 300 + ((vinicial*vinicial)*(math.sin(ang1)*math.sin(ang1))/(2*9.81))

    return alcance, alturamax

alcance1, alturamaxima1 = criticos(30,100)
print(alturamaxima1)

init()
screen = display.set_mode((800,600))
animar1 = False
animar2 = False
animar3 = False
clock = time.Clock()
calibri = font.SysFont('Calibri', 20)

while True:
    screen.fill((255,255,255))
    fondo = transform.scale(image.load("fondo.jpg"), (800,600))
    volcan = transform.scale(image.load("volcan.png"), (300,300))
    for e in event.get():
        if e.type == QUIT: sys.exit()
        clock.tick(15)
        if e.type == KEYDOWN and e.key == K_1:
            animar1 = True
        if e.type == KEYDOWN and e.key == K_2:
            animar2 = True
        if e.type == KEYDOWN and e.key == K_3:
            animar3 = True 
    
    leyenda1 = calibri.render("Trayectoria actual: ", True, (0,0,0))
    screen.blit(leyenda1, (0,0))
    leyenda2 = calibri.render("Alcance máximo: ", True, (0,0,0))
    screen.blit(leyenda2, (0,20))
    leyenda3 = calibri.render("Altura máxima: ", True, (0,0,0))
    screen.blit(leyenda3, (0,40))
    screen.blit(fondo, (0,0))
    screen.blit(volcan, (-120,310))
    if animar1: 
        x1, y1 = coord(30,100)
        anim(x1, y1)
        xr1, yr1 = resistencia(30,100, 0)
        animr(xr1,yr1)
    if animar2:
        x2, y2 = coord(41, 175)
        anim(x2,y2)
    if animar3:
        x3, y3 = coord(44,300)
        anim(x3,y3) 
    display.flip()