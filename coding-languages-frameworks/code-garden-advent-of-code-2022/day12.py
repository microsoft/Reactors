#!/usr/bin/env python3
from string import ascii_lowercase

data = [x.strip() for x in open("day12-data.txt").readlines()]

start = None
target = None
cells = {}

for y, row in enumerate(data):
    for x, cell in enumerate(row):
        if cell == "S":
            start = (x, y)
            cells[(x, y)] = 0
        elif cell == "E":
            target = (x, y)
            cells[(x, y)] = 25
        else:
            cells[(x, y)] = ascii_lowercase.index(cell)
            
def adjacentCells(cell):
    x, y = cell
    allAdjacents = []
    if (x-1, y) in cells:
        allAdjacents.append((x-1, y))
    if (x+1, y) in cells:
        allAdjacents.append((x+1, y))
    if (x, y-1) in cells:
        allAdjacents.append((x, y-1))
    if (x, y+1) in cells:
        allAdjacents.append((x, y+1))
    return allAdjacents

def canMove(fromCell, toCell):
    return cells[toCell] <= cells[fromCell]+1

def findPath(start):
    current = start
    shortestPaths = {start: 0}
    
    cellsToCheck = [start]
    history = set()
    
    while cellsToCheck:
        current = cellsToCheck.pop(0)
        steps = shortestPaths[current]
        
        history.add(current)
        adjCells = adjacentCells(current)
        validCells = [c for c in adjCells if canMove(current, c)]
        
        for c in validCells:
            if c not in history and c not in cellsToCheck:
                cellsToCheck.append(c)
        
            if c in shortestPaths:
                shortestPaths[c] = min(steps+1, shortestPaths[c])
            else:
                shortestPaths[c] = steps+1
    
    if target not in shortestPaths:
        return len(cells)
    return shortestPaths[target]

part1 = findPath(start)
print(part1)


shortestPath = part1
bestStart = start

allACells = [c for c in cells.keys() if cells[c] == 0]

for aCell in allACells:
    dist = findPath(aCell)
    if dist < shortestPath:
        shortestPath = dist
        bestStart = aCell

print(bestStart, shortestPath)