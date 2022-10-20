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

def resistencia(ang, vinicial):
    ang1 = math.radians(ang)
    vox = vinicial*math.cos(ang1)
    voy =  vinicial*math.sin(ang1)
    av = vinicial/2
    xcoordr = []
    ycoordr = []
    t = 0
    
    while t < 1000:
        y1 = vox*t + ((av*t*t)/2)
        yr = voy*t + ((-9.81*t*t)/2)
        t = t + 50
        ycoordr.append(y1)
        xcoordr.append(x1)
    return xcoordr, ycoordr


def anim(xcoord, ycoord):
    puntos = 0
    while puntos < len(xcoord):
        draw.rect(screen, (255,0,0), (xcoord[puntos], 300-ycoord[puntos], 10,10), 3)
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
animar = False
clock = time.Clock()
calibri = font.SysFont('Calibri', 20)

while True:
    screen.fill((255,255,255))
    for e in event.get():
        if e.type == QUIT: sys.exit()
        clock.tick(15)
        if e.type == KEYDOWN and e.key == K_1:
            animar = True
    
    leyenda1 = calibri.render("Trayectoria actual: ", True, (0,0,0))
    screen.blit(leyenda1, (0,0))
    leyenda2 = calibri.render("Alcance máximo: ", True, (0,0,0))
    screen.blit(leyenda2, (0,20))
    leyenda3 = calibri.render("Altura máxima: ", True, (0,0,0))
    screen.blit(leyenda3, (0,40))
    if animar: 
        x1, y2 = coord(30,100)
        anim(x1, y2)
        alcance1, alturamaxima1 = criticos(30,100)
        print(alturamaxima1)
        x1r, y1r = resistencia(30,100)
        anim(x1r, y1r)
        #valor1 = calibri.render(alcance1, True, (0,0,0)) 
        #valor2 = calibri.render(alturamaxima1, True, (0,0,0)) 
        #screen.blit(10,20)
        #screen.blit(10,40)
    
    display.flip()