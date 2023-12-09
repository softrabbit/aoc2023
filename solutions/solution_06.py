import functools
from operator import mul
import sys
sys.path.append("..")

from aoclib import util

# Boats move faster if their button was held longer, but time spent
# holding the button counts against the total race time. You can only
# hold the button at the start of the race, and boats don't move until
# the button is released.
# Determine the number of ways you could beat the record in each race.
# What do you get if you multiply these numbers together?
def solve_06(data):
    ways = []
    for line in data:
        if line.startswith("Time:"):
            times = list(map(int,line.split()[1:]))
        elif line.startswith("Distance:"):
            records = list(map(int,line.split()[1:]))

    for i in range(0,len(times)):
        t = times[i]
        d = records[i]
        # count the number of ways to beat the record
        w = 0
        for x in range(1,t+1):
            if (t-x) * x > d:
                w += 1   
        ways.append(w)
    return functools.reduce(mul,ways,1)

# Oops, the input isn't in lists, but spaced out ints, 
# e.g. "3 14 1 592" -> 3141592.
# That actually simplifies things.
def solve_06b(data):
    for line in data:
        if line.startswith("Time:"):
            time = int(''.join(line.split()[1:]))
        elif line.startswith("Distance:"):
            record = int(''.join(line.split()[1:]))

    w = 0
    for x in range(1,time+1):
        if (time-x) * x > record:
            w += 1   
    return w
    

if __name__ == '__main__':
    data = util.getInput("../inputs/06.txt")
    print( solve_06(data) )
    print( solve_06b(data) )

