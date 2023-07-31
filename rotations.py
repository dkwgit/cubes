import numpy as np

refArray = np.zeros((3,3,3))
refIndexMap = {}
val = 1
for x in range (3):
  for y in range(3):
    for z in range(3):
      refArray[x,y,z] = val
      refIndexMap[val] = (x,y,z)
      val = val + 1

arrayCopy = np.rot90(refArray, 1, (1,2))
copyIndexMap = {}
val = 1
for x in range (3):
  for y in range(3):
    for z in range(3):
      val = arrayCopy[x,y,z]
      copyIndexMap[val] = (x,y,z)
      val = val + 1
      
for i in range(1, 28):
  xRef, yRef, zRef = refIndexMap[i]
  xCopy, yCopy, zCopy = copyIndexMap[i]
  diff = (xCopy - xRef, yCopy - yRef, zCopy - zRef)
  print(i,(xRef,yRef,zRef),(xCopy, yCopy, zCopy),diff)
  