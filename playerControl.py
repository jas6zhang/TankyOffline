from math import *



class playerControl(object):
    def __init__(self):
        self.X = -100
        self.Y = -300
        self.angle = 0
        self.Exists = False
        self.projectiles = 0
    
    def spawn(self,x,y):
        if not self.Exists:
            self.X = x
            self.Y = y
            self.Exists = True
    
    def move(self,w,a,s,d,walls):
        if self.Exists:
            if w:
                move = True
                bufferx = float(self.X)
                buffery = float(self.Y)
                for speed in range(0,4):
                    bufferx += cos(self.angle)
                    buffery -= sin(self.angle)
                    for wall in walls:
                        if ((wall[0]-bufferx)**2 + (wall[1]-buffery)**2)**.5 < 24:
                            move = False
                            break
                        elif ((wall[0]+64-bufferx)**2 + (wall[1]-buffery)**2)**.5 < 24:
                            move = False
                            break
                        elif ((wall[0]-bufferx)**2 + (wall[1]+64-buffery)**2)**.5 < 24:
                            move = False
                            break
                        elif ((wall[0]+64-bufferx)**2 + (wall[1]+64-buffery)**2)**.5 < 24:
                            move = False
                            break
                        elif round(bufferx) in [wall[0] - 24,wall[0] + 88] and round(buffery) in range(wall[1],wall[1] + 64):
                            move = False
                            break
                        elif round(buffery) in [wall[1] - 24,wall[1] + 88] and round(bufferx) in range(wall[0],wall[0] + 64):
                            move = False
                            break
                    if round(bufferx) in [23,1001]:
                        move = False
                    if round(buffery) in [23,677]:
                        move = False
                if move:
                    self.X = round(bufferx)
                    self.Y = round(buffery)
            if a:
                self.angle += pi/64
            if d:
                self.angle -= pi/64
            if s:
                move = True
                bufferx = float(self.X)
                buffery = float(self.Y)
                for speed in range(0,4):
                    bufferx += cos(pi + self.angle)
                    buffery -= sin(pi + self.angle)
                    for wall in walls:
                        if ((wall[0]-bufferx)**2 + (wall[1]-buffery)**2)**.5 < 24:
                            move = False
                            break
                        elif ((wall[0]+64-bufferx)**2 + (wall[1]-buffery)**2)**.5 < 24:
                            move = False
                            break
                        elif ((wall[0]-bufferx)**2 + (wall[1]+64-buffery)**2)**.5 < 24:
                            move = False
                            break
                        elif ((wall[0]+64-bufferx)**2 + (wall[1]+64-buffery)**2)**.5 < 24:
                            move = False
                            break
                        elif round(bufferx) in [wall[0] - 24,wall[0] + 88] and round(buffery) in range(wall[1],wall[1] + 64):
                            move = False
                            break
                        elif round(buffery) in [wall[1] - 24,wall[1] + 88] and round(bufferx) in range(wall[0],wall[0] + 64):
                            move = False
                            break
                    if round(bufferx) in [23,1001]:
                        move = False
                    if round(buffery) in [23,677]:
                        move = False
                if move:
                    self.X = round(bufferx)
                    self.Y = round(buffery)
    
    def collide(self,target):
        if self.Exists:
            if ((self.X - target.X)**2 + (self.Y - target.Y)**2)**.5 <= 32:
                if target.exists:
                    self.Exists = False
                    target.exists = False
                    self.X = -100
                    self.Y = -300
                    target.X = -100
                    target.Y = -100
