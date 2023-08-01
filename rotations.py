import numpy as np

def createArrayWithIndexMap(xDim, yDim, zDim):
  theArray = np.zeros((xDim,yDim,zDim), dtype=np.int64)
  theIndexMap = {}
  val = 1
  for x in range (xDim):
    for y in range(yDim):
      for z in range(zDim):
        theArray[x,y,z] = val
        theIndexMap[val] = (x,y,z)
        val = val + 1
  return (theArray, theIndexMap)

def rotateArray(arrayToRotate, increment, axes):
  newArray = np.rot90(arrayToRotate, increment, axes)
  xDim, yDim, zDim = np.shape(newArray)
  newIndexMap = {}
  for x in range (xDim):
    for y in range(yDim):
      for z in range(zDim):
        val = newArray[x,y,z]
        newIndexMap[val] = (x,y,z)
  return (newArray, newIndexMap)
      
def testX90(tuple):
  orig, origIndexMap = tuple
  xDim, yDim, zDim = np.shape(orig)
  newArray, newIndexMap = rotateArray(orig, 1, (1,2))
  for i in range(1, xDim * yDim * zDim + 1):
    x, y, z = origIndexMap[i]
    xNew, yNew, zNew = newIndexMap[i]
    diff = (x - xNew, zDim - z - 1 - yNew, y - zNew)
    print("testX90", i, (x,y,z), (xNew, yNew, zNew), diff)
  print("\n")
  
def testX180(tuple):  
  orig, origIndexMap = tuple
  xDim, yDim, zDim = np.shape(orig)
  newArray, newIndexMap = rotateArray(orig, 2, (1,2))
  for i in range(1, xDim * yDim * zDim + 1):
    x, y, z = origIndexMap[i]
    xNew, yNew, zNew = newIndexMap[i]
    diff = (x - xNew, yDim - y - 1 - yNew, zDim - z - 1 - zNew)
    print("testX180", i, (x,y,z), (xNew, yNew, zNew), diff)
  print("\n")
  
def testX270(tuple):  
  orig, origIndexMap = tuple
  xDim, yDim, zDim = np.shape(orig)
  newArray, newIndexMap = rotateArray(orig, 3, (1,2))
  for i in range(1, xDim * yDim * zDim + 1):
    x, y, z = origIndexMap[i]
    xNew, yNew, zNew = newIndexMap[i]
    diff = (x - xNew, z - yNew, yDim - y - 1 - zNew)
    print("testX270", i, (x,y,z), (xNew, yNew, zNew), diff)
  print("\n")
  
def testY90(tuple):
  orig, origIndexMap = tuple
  xDim, yDim, zDim = np.shape(orig)
  newArray, newIndexMap = rotateArray(orig, -1, (0,2))
  for i in range(1, xDim * yDim * zDim + 1):
    x, y, z = origIndexMap[i]
    xNew, yNew, zNew = newIndexMap[i]
    diff = (z - xNew, y - yNew, xDim - x - 1 - zNew)
    print("testY90", i, (x,y,z), (xNew, yNew, zNew), diff)
  print("\n")
  
def testY180(tuple):  
  orig, origIndexMap = tuple
  xDim, yDim, zDim = np.shape(orig)
  newArray, newIndexMap = rotateArray(orig, -2, (0,2))
  for i in range(1, xDim * yDim * zDim + 1):
    x, y, z = origIndexMap[i]
    xNew, yNew, zNew = newIndexMap[i]
    diff = (xDim - x - 1 - xNew, y - yNew, zDim - z - 1 - zNew)
    print("testY180", i, (x,y,z), (xNew, yNew, zNew), diff)
  print("\n")
  
def testY270(tuple):  
  orig, origIndexMap = tuple
  xDim, yDim, zDim = np.shape(orig)
  newArray, newIndexMap = rotateArray(orig, -3, (0,2))
  for i in range(1, xDim * yDim * zDim + 1):
    x, y, z = origIndexMap[i]
    xNew, yNew, zNew = newIndexMap[i]
    diff = (zDim - z - 1 - xNew, y - yNew, x - zNew)
    print("testY270", i, (x,y,z), (xNew, yNew, zNew), diff)
  print("\n")
  
def testZ90(tuple):
  orig, origIndexMap = tuple
  xDim, yDim, zDim = np.shape(orig)
  newArray, newIndexMap = rotateArray(orig, -1, (0,1))
  for i in range(1, xDim * yDim * zDim + 1):
    x, y, z = origIndexMap[i]
    xNew, yNew, zNew = newIndexMap[i]
    diff = (y - xNew, xDim - x- 1 - yNew, z - zNew)
    print("testZ90", i, (x,y,z), (xNew, yNew, zNew), diff)
  print("\n")
  
def testZ180(tuple):  
  orig, origIndexMap = tuple
  xDim, yDim, zDim = np.shape(orig)
  newArray, newIndexMap = rotateArray(orig, -2, (0,1))
  for i in range(1, xDim * yDim * zDim + 1):
    x, y, z = origIndexMap[i]
    xNew, yNew, zNew = newIndexMap[i]
    diff = (xDim - x -1 - xNew, yDim - y - 1 - yNew, z - zNew)
    print("testZ180", i, (x,y,z), (xNew, yNew, zNew), diff)
  print("\n")
  
def testZ270(tuple):  
  orig, origIndexMap = tuple
  xDim, yDim, zDim = np.shape(orig)
  newArray, newIndexMap = rotateArray(orig, -3, (0,1))
  for i in range(1, xDim * yDim * zDim + 1):
    x, y, z = origIndexMap[i]
    xNew, yNew, zNew = newIndexMap[i]
    diff = (yDim - y - 1 - xNew, x - yNew, z - zNew)
    print("testZ270", i, (x,y,z), (xNew, yNew, zNew), diff)
  print("\n")
  
def main():
  tuple = createArrayWithIndexMap(3,2,4)
  testX90(tuple)
  testX180(tuple)
  testX270(tuple)
  testY90(tuple)
  testY180(tuple)
  testY270(tuple)
  testZ90(tuple)
  testZ180(tuple)
  testZ270(tuple)
  
  
if __name__ == "__main__":
  main()