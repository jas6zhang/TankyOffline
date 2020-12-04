from math import *

class projectile(object):
    def __init__(self,bulletnum):
        self.X = -100
        self.Y = -100
        self.time = 0
        self.angle = 0
        self.exists = False
        self.ID = bulletnum
    
    def shoot(self,target,angle):
        if target.projectiles == self.ID and not self.exists:
            self.X = target.X + round(33*cos(angle))
            self.Y = target.Y - round(33*sin(angle))
            self.angle = angle
            self.time = 300
            self.exists = True
            target.projectiles = (target.projectiles + 1) % 5
            return True
        else:
            return False
    
    def projMove(self,walls):
        if self.exists:
            xbuffer = float(self.X)
            ybuffer = float(self.Y)
            for speed in range(0,10):
                xbuffer += cos(self.angle)
                ybuffer -= sin(self.angle)
                for wall in walls:
                    if round(xbuffer) in range(wall[0],wall[0] + 64) and round(ybuffer) in range(wall[1],wall[1] + 64):
                        if xbuffer - wall[0] < 1 or wall[0] + 64 - xbuffer < 1:
                            self.angle = pi - self.angle
                        else:
                            self.angle *= -1
                if round(xbuffer) in [0,1024]:
                    self.angle = pi - self.angle
                if round(ybuffer) in [0,704]:
                    self.angle *= -1
            self.X = round(xbuffer)
            self.Y = round(ybuffer)
    
    def decay(self):
        self.time -= 1
        if self.time == 0:
            self.exists = False
            self.X = -100
            self.Y = -100
            self.time = 0
            self.angle = 0