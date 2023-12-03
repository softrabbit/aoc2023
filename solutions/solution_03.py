import sys
sys.path.append("..")

from aoclib import util
import re

# The engine schematic (your puzzle input) consists of a visual
# representation of the engine. There are lots of numbers and symbols
# you don't really understand, but apparently any number adjacent to 
# a symbol, even diagonally, is a "part number" and should be included 
# in your sum. (Periods (.) do not count as a symbol.)

def solve_03(data):
    sum = 0
    for i in range(0, len(data) ):        
        matches = re.finditer(r"[0-9]+", data[i])
        for m in matches:
            
            start = max(0,m.start()-1)
            stop = min(len(data[i]),m.end()+1)
            
            for j in range(max(0,i-1), min(len(data), i+2)):                
                if re.search(r"[^0-9\.]", data[j][start:stop]) is not None:
                    sum += int(m.group())
                    break
                                    
    return sum

# A gear is any * symbol that is adjacent to exactly two part numbers. 
# Its gear ratio is the result of multiplying those two numbers together.
# This time, you need to find the gear ratio of every gear and add them 
# all up so that the engineer can figure out which gear needs to be replaced.
def solve_03b(data):
    sum = 0
    for i in range(0, len(data) ):        
        matches = re.finditer(r"\*", data[i])
        for mstar in matches:
            spot = mstar.start()
            numbers = []
            for j in range(max(0,i-1), min(len(data),i+2) ):
                num_matches = re.finditer(r"[0-9]+", data[j])
                for candidate in num_matches:
                    if candidate.start() < spot + 2 and candidate.end() > spot - 1:
                        numbers.append(int(candidate.group()))
                
            if len(numbers) == 2:
                sum += numbers[0] * numbers[1]

    return sum


if __name__ == '__main__':
    data = util.getInput("../inputs/03.txt")
    print( solve_03(data) )
    print( solve_03b(data) )
