from pygame import *
from math import *
from playerControl import *
from projectile import *
from mapGen import *
import os 

os.environ['SDL_VIDEO_CENTERED'] = '1'

init()
running = True

screen = display.set_mode((1024,704))
clock = time.Clock()

world = gameMap(0,0,1024,702,3)
world.mapgen(screen,0,0)

p1 = playerControl()
p2 = playerControl()
p1.spawn(32,32)
p2.spawn(996,672)
p1b1 = projectile(0)
p1b2 = projectile(1)
p1b3 = projectile(2)
p1b4 = projectile(3)
p1b5 = projectile(4)
p2b1 = projectile(0)
p2b2 = projectile(1)
p2b3 = projectile(2)
p2b4 = projectile(3)
p2b5 = projectile(4)

pList = [p1b1,p1b2,p1b3,p1b4,p1b5,p2b1,p2b2,p2b3,p2b4,p2b5]

blocks = world.get_wallist()

wDown = False
aDown = False
sDown = False
dDown = False
upDown = False
leftDown = False
rightDown = False
downDown = False

while running:
    for evnt in event.get():
        if evnt.type == QUIT:
            running = False
        if evnt.type == KEYDOWN:
            if evnt.key == K_w:
                wDown = True
            if evnt.key == K_a:
                aDown = True
            if evnt.key == K_s:
                sDown = True
            if evnt.key == K_d:
                dDown = True
            if evnt.key == K_UP:
                upDown = True
            if evnt.key == K_LEFT:
                leftDown = True
            if evnt.key == K_RIGHT:
                rightDown = True
            if evnt.key == K_DOWN:
                downDown = True
            if evnt.key == K_SPACE:
                for p in pList[:5]:
                    if p.shoot(p1,p1.angle):
                        break
            if evnt.key == K_RETURN:
                for p in pList[5:]:
                    if p.shoot(p2,p2.angle):
                        break
        if evnt.type == KEYUP:
            if evnt.key == K_w:
                wDown = False
            if evnt.key == K_a:
                aDown = False
            if evnt.key == K_s:
                sDown = False
            if evnt.key == K_d:
                dDown = False
            if evnt.key == K_UP:
                upDown = False
            if evnt.key == K_LEFT:
                leftDown = False
            if evnt.key == K_RIGHT:
                rightDown = False
            if evnt.key == K_DOWN:
                downDown = False
    
    p1.move(wDown,aDown,sDown,dDown,blocks)
    p2.move(upDown,leftDown,downDown,rightDown,blocks)
    
    for p in pList:
        p.projMove(blocks)
        p.decay()
        p1.collide(p)
        p2.collide(p)
    
    world.background(screen,0,0,64)
    draw.circle(screen,(0,0,255),(p1.X,p1.Y),24)
    draw.line(screen,(0,0,0),(p1.X,p1.Y),(p1.X + round(20*cos(p1.angle)),p1.Y - round(20*sin(p1.angle))),5)
    draw.circle(screen,(255,0,0),(p2.X,p2.Y),24)
    draw.line(screen,(0,0,0),(p2.X,p2.Y),(p2.X + round(20*cos(p2.angle)),p2.Y - round(20*sin(p2.angle))),5)
    for p in pList:
        draw.circle(screen,(255,255,255),(p.X,p.Y),3)
    for block in blocks:
        draw.rect(screen,(0,255,0),block + (64,64))
    
    display.flip()
    clock.tick(60)
    if p1.Exists == False or p2.Exists == False:
        running = False

quit()
