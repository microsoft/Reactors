#!/usr/bin/env python3
from math import sqrt

steps = [x.strip().split(" ") for x in open("day9-data.txt").readlines()]

U = (0,1)
D = (0, -1)
L = (-1, 0)
R = (1, 0)

dirs = {"U":U, "D":D, "L":L, "R":R}

class Rope:
    def __init__(self, head=(0,0), tail=(0,0), nextRope=None):
        self.head = head
        self.tail = tail
        self.nextRope = nextRope
        self.tailLog = {tail}

    def attachRope(self, rope):
        self.nextRope = rope

    def ropeLength(self):
        a = self.head[0] - self.tail[0]
        b = self.head[1] - self.tail[1]
        return sqrt(a**2 + b**2)

    def moveHead(self, dir):
        self.head = (self.head[0] + dir[0], self.head[1] + dir[1])
        self.catchUpTail()
        
    def setHead(self, pos):
        self.head = pos
        self.catchUpTail()
        
    def catchUpTail(self):
        rLen = self.ropeLength()
        if rLen < 2:
            # close enough
            pass
        elif rLen == 2:
            # linear offset
            if self.tail[0] == self.head[0]:
                # x pos is the same
                if self.tail[1] < self.head[1]:
                    self.tail = (self.tail[0] + U[0], self.tail[1] + U[1])
                else:
                    self.tail = (self.tail[0] + D[0], self.tail[1] + D[1])
            else:
                # y pos is the same
                if self.tail[0] < self.head[0]:
                    self.tail = (self.tail[0] + R[0], self.tail[1] + R[1])
                else:
                    self.tail = (self.tail[0] + L[0], self.tail[1] + L[1])
        else:
            # it's diagonally away
            if self.tail[1] < self.head[1]:
                self.tail = (self.tail[0] + U[0], self.tail[1] + U[1])
            else:
                self.tail = (self.tail[0] + D[0], self.tail[1] + D[1])
            if self.tail[0] < self.head[0]:
                self.tail = (self.tail[0] + R[0], self.tail[1] + R[1])
            else:
                self.tail = (self.tail[0] + L[0], self.tail[1] + L[1])
        self.tailLog.add(self.tail)
        
        if self.nextRope:
            self.nextRope.setHead(self.tail)

firstRope = Rope()
lastRope = firstRope

for i in range(8):
    newRope = Rope()
    lastRope.attachRope(newRope)
    lastRope = newRope

for d, c in steps:
    for i in range(int(c)):
        firstRope.moveHead(dirs[d])

print(len(lastRope.tailLog))

