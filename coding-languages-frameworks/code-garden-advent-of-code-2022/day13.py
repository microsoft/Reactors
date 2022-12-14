#!/usr/bin/env python3
from json import loads
from functools import cmp_to_key

INORDER = 1
OUTORDER = -1
EQUAL = 0

fname = "day13-data.txt"

pairs = [x.strip().split("\n") for x in open(fname).read().split("\n\n")]

def compareList(left, right):
    for i, l in enumerate(left):
        if i >= len(right):
            return OUTORDER
        
        r = right[i]
        
        if type(l) == int and type(r) == int:
            if l < r:
                return INORDER
            elif l > r:
                return OUTORDER
        else:
            if type(l) == int:
                l = [l]
            if type(r) == int:
                r = [r]
            subComp = compareList(l, r)
            if subComp:
                return subComp
    
    if len(right) > len(left):
        return INORDER
    return EQUAL

goodSum = 0
for i, p in enumerate(pairs):
    left = loads(p[0])
    right = loads(p[1])
    if compareList(left, right) == 1:
        goodSum += i+1
    
print(goodSum)

allSignals = [loads(x.strip()) for x in open(fname).read().split("\n") if x]

allSignals.append([[2]])
allSignals.append([[6]])

allSignals.sort(key=cmp_to_key(compareList), reverse=True)

div1Index = allSignals.index([[2]]) + 1
div2Index = allSignals.index([[6]]) + 1
print(div1Index * div2Index)