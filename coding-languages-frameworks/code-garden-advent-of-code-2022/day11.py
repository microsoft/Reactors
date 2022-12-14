#!/usr/bin/env python3

data = [x.strip() for x in open("day11-data.txt").readlines()]

class Monkey:
    allMonkeys = []
    lcm = 1
    
    def monkey(i):
        return Monkey.allMonkeys[i]
    
    def __init__(self, items, op, test, tRecipient, fRecipient):
        self.items = items
        self.op = op
        self.test = test
        self.tRecipient = tRecipient
        self.fRecipient = fRecipient
        self.inspections = 0
        Monkey.allMonkeys.append(self)
        
    def turn(self):
        self.inspections += len(self.items)
        for i in self.items:
            i = self.op(i)
#           i //= 3
            i %= Monkey.lcm
            if self.test(i):
                self.giveItem(i, Monkey.allMonkeys[self.tRecipient])
            else:
                self.giveItem(i, Monkey.allMonkeys[self.fRecipient])
        self.items = []
        
    def giveItem(self, i, recipient):
        recipient.items.append(i)

for i in range(0, len(data), 7):
#   Monkey 0:
#       Starting items: 79, 98
    startingItemsData = data[i+1].split(": ")[1]
    startingItems = [int(x) for x in startingItemsData.split(", ")]
#       Operation: new = old * 19
    operationStr = data[i+2].split(" = ")[1]
    a, op, b = operationStr.split(" ")
    if op == "+":
        if b.isnumeric():
            operationFunc = lambda x, b=int(b): x + b
        else:
            operationFunc = lambda x: x + x
    elif op == "*":
        if b.isnumeric():
            operationFunc = lambda x, b=int(b): x * b
        else:
            operationFunc = lambda x: x * x
#       Test: divisible by 23
    modNum = int(data[i+3].split(" ")[-1])
    Monkey.lcm *= modNum
    testFunc = lambda x, m=modNum: x % m == 0
#           If true: throw to monkey 2
    tRecipient = int(data[i+4].split(" ")[-1])
#           If false: throw to monkey 3
    fRecipient = int(data[i+5].split(" ")[-1])
    
    Monkey(startingItems, operationFunc, testFunc, tRecipient, fRecipient)

for i in range(20):
    print("Round", i+1)
    for m in Monkey.allMonkeys:
        m.turn()
    for m in Monkey.allMonkeys:
        print(m.items)

inspections = sorted([m.inspections for m in Monkey.allMonkeys])
print(inspections)
print(inspections[-1] * inspections[-2])

for i in range(20, 10000):
    print("Round", i+1)
    for m in Monkey.allMonkeys:
        m.turn()
    for m in Monkey.allMonkeys:
        print(m.items)

inspections = sorted([m.inspections for m in Monkey.allMonkeys])
print(inspections)
print(inspections[-1] * inspections[-2])

# 15105064777 too high
# 13937702909 correct!