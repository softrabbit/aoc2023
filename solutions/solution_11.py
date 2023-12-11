import sys
sys.path.append("..")

from aoclib import util
import numpy as np

# Expand the universe, then find the length of the shortest path
# between every pair of galaxies. What is the sum of these lengths?
def solve_11(data):
    # Expand the universe...
    universe = np.char.array(data)
    # ...by inserting empty lines     
    inserted = 0
    for i, galaxycount in enumerate(universe.count('#')):
        if galaxycount == 0:
               universe = np.insert(universe, i+inserted, '.' * len(universe[i]))
               inserted += 1
    
    # ...and columns
    universe = np.rot90(universe.view('U1').reshape(universe.size,-1))  
    inserted = 0
    for i, line in enumerate(universe):
        chr,counts = np.unique(line, return_counts=True)
        counts = dict(zip(chr, counts))
        if not '#' in counts:             
             # The axis thing because we now have a 2D array of char...
             universe = np.insert(universe,i+inserted, line, axis=0)
             inserted += 1

    tmp = np.where(universe == '#')
    positions = list(zip(tmp[0],tmp[1]))

    distances = np.zeros((len(positions),len(positions)),dtype=np.int32)
    # quadratic time, but is there any other way?
    for i in range(0,len(positions)):
         for j in range(i+1,len(positions)):
            # Manhattan distance
            distances[i][j] = abs(positions[i][0] - positions[j][0]) + abs(positions[i][1] - positions[j][1])
                    

    print(positions)
    print(distances)

    print(universe)
    print(universe.shape)
    return sum(sum(distances))

# As the first part, but now expand empty rows/columns by one million...
def solve_11b(data, factor=1000000):    
    # Expand the universe...
    universe = np.char.array(data)
    # ...by inserting empty lines     
    inserted = 0
    for i, galaxycount in enumerate(universe.count('#')):
        if galaxycount == 0:
               universe = np.insert(universe, i+inserted, '.' * len(universe[i]))
               inserted += 1
    
    # ...and columns
    universe = np.rot90(universe.view('U1').reshape(universe.size,-1))  
    inserted = 0
    for i, line in enumerate(universe):
        chr,counts = np.unique(line, return_counts=True)
        counts = dict(zip(chr, counts))
        if not '#' in counts:             
             # The axis thing because we now have a 2D array of char...
             universe = np.insert(universe,i+inserted, line, axis=0)
             inserted += 1

    tmp = np.where(universe == '#')
    positions = list(zip(tmp[0],tmp[1]))

    distances = np.zeros((len(positions),len(positions)),dtype=np.int32)
    # quadratic time, but is there any other way?
    for i in range(0,len(positions)):
         for j in range(i+1,len(positions)):
            # Manhattan distance
            distances[i][j] = abs(positions[i][0] - positions[j][0]) + abs(positions[i][1] - positions[j][1])
                    

    print(positions)
    print(distances)

    print(universe)
    print(universe.shape)
    return sum(sum(distances))


if __name__ == '__main__':
    data = util.getInput("../inputs/11.txt")
    print( solve_11(data) )
    print( solve_11b(data) )
