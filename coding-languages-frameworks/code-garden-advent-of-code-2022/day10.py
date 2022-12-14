#!/usr/bin/env python3

instructions = [x.strip() for x in open("day10-data.txt").readlines()]

class CPU:
    def __init__(self):
        self.clock = 0
        self.X = 1
        self.signal_beats = []
        self.display = []
    
    def log(self):
        if (self.clock+20) % 40 == 0:
            print(self.clock, self.X, self.signal_strength())
            self.signal_beats.append(self.signal_strength())
    
    def setPixel(self):
        if abs(self.clock%40 - self.X) <= 1:
            self.display.append('#')
        else:
            self.display.append('.')
    
    def drawDisplay(self):
        for i in range(self.clock):
            if i % 40 == 0:
                print()
            print(self.display[i], end="")
    
    def step(self):
        self.setPixel()
        self.clock += 1
        self.log()
        
    def noop(self):
        self.step()
    
    def addx(self, val):
        self.step()
        self.step()
        self.X += val
        
    def signal_strength(self):
        return self.clock * self.X

cpu = CPU()

for i in instructions:
    #print(">", i)
    if i == "noop":
        cpu.noop()
    elif i.startswith("addx"):
        val = int(i.split(" ")[1])
        cpu.addx(val)
        #print(">>", cpu.clock, cpu.X)

print("Signal sum:", sum(cpu.signal_beats))

cpu.drawDisplay()


# Renee's code
# x = 1
# cycle_x = []

# with open("day10-data.txt") as f:
#     for line in f:
#         inst = line.strip().split(" ")

#         if inst[0] == "noop":
#             cycle_x.append(x)

#         else:
#             num = inst[1]
#             cycle_x.append(x)
#             cycle_x.append(x)
#             x += int(num)
            

# total = 0
# for i in range(19, len(cycle_x), 40):
#     print(cycle_x[i - 1], i + 1)
#     total += cycle_x[i - 1] * (i + 1)

# print(total)

# for i, x in enumerate(cycle_x):
#     if i%40 == x-1 or i%40 == x or i%40 == x + 1:
#         print("#", end="")
#     else:
#         print(".", end="")

#     if i + 1 in list(range(0, len(cycle_x), 40)):
#         print()
