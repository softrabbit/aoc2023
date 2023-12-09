import sys
sys.path.append("..")

from aoclib import util

from enum import Enum
class Edge (Enum):
    left = 1
    right = 2

# Your environmental report should include a prediction of the next value
# in each history. To do this, start by making a new sequence from the
# difference at each step of your history. If that sequence is not all
# zeroes, repeat this process, using the sequence you just generated as
# the input sequence. Once all of the values in your latest sequence are
# zeroes, you can extrapolate what the next value of the original history
# should be.

# Do the summing and reduction, recurse, return the number to add to the list
# The returned number is added to the left or right edge of the list
# according to some rules. (See the AoC site for details)
def deltareduce(nums, edge):
    # The recursion stops here
    if len(nums) == 1 or set(nums) == {0}:
        return 0
    next = [ nums[i+1] - nums[i] for i in range(len(nums)-1)]    
    
    if edge == Edge.right:
        return nums[-1] +deltareduce(next,edge)
    elif edge == Edge.left:
        return nums[0] - deltareduce(next,edge)
    else:
        assert False
    

# Extrapolate the next value for each history.
# What is the sum of these extrapolated values
def solve_09(data, edge = Edge.right):
    sum = 0
    for line in data:
        nums = list(map(int,line.split()))
        sum += deltareduce(nums, edge)
    return sum

if __name__ == '__main__':
    data = util.getInput("../inputs/09.txt")
    print( solve_09(data, Edge.right) )
    print( solve_09(data, Edge.left) ) 

