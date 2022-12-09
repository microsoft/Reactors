#!/usr/bin/env python3

data = [x.strip() for x in open("day8-data.txt").readlines()]

maxY = len(data)
maxX = len(data[0])

trees = {}

for y in range(maxY):
  for x in range(maxX):
    trees[(x,y)] = int(data[y][x])
    
def isVisible(treeX, treeY):
  treeHeight = trees[(treeX, treeY)]
  
  if treeX == 0 or treeY == 0 or treeX == maxX-1 or treeY == maxY-1:
    # is boundary tree
    return True
  
  vis = True
  for x in range(0, treeX):
    # can be seen from the left
    if trees[(x, treeY)] >= treeHeight:
      vis = False
      break
  if vis:
    return True
  
  vis = True
  for x in range(treeX+1, maxX):
    # can be seen from the right
    if trees[(x, treeY)] >= treeHeight:
      vis = False
      break
  if vis:
    return True
  
  vis = True
  for y in range(0, treeY):
    # can be seen from the top
    if trees[(treeX, y)] >= treeHeight:
      vis = False
      break
  if vis:
    return True
  
  vis = True
  for y in range(treeY+1, maxY):
    # can be seen from the bottom
    if trees[(treeX, y)] >= treeHeight:
      vis = False
      break
  if vis:
    return True
  
  return False

visibleTrees = 0
for x, y in trees.keys():
  visibleTrees += isVisible(x, y)
print(visibleTrees)

def upVis(x, treeY, h):
  score = 0
  for y in range(treeY-1, -1, -1):
    if trees[(x, y)] < h:
      score += 1
    else:
      score += 1
      return score
  return score

def downVis(x, treeY, h):
  score = 0
  for y in range(treeY+1, maxY):
    if trees[(x, y)] < h:
      score += 1
    else:
      score += 1
      return score
  return score

def leftVis(treeX, y, h):
  score = 0
  for x in range(treeX-1, -1, -1):
    if trees[(x, y)] < h:
      score += 1
    else:
      score += 1
      return score
  return score

def rightVis(treeX, y, h):
  score = 0
  for x in range(treeX+1, maxX):
    if trees[(x, y)] < h:
      score += 1
    else:
      score += 1
      return score
  return score

def visScore(x, y):
  h = trees[(x, y)]
  return upVis(x, y, h) * downVis(x, y, h) * leftVis(x, y, h) * rightVis(x, y, h)

bestScore = 0
bestPos = None

for x, y in trees.keys():
  if x == 2 and y == 3:
    pass
  score = visScore(x, y)
  if score > bestScore:
    bestPos = (x, y)
    bestScore = score
    
print(bestPos, bestScore)