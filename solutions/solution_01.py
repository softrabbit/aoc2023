import sys
sys.path.append("..")

from aoclib import util
import re

# The newly-improved calibration document consists of lines of text; 
# each line originally contained a specific calibration value that the 
# Elves now need to recover. On each line, the calibration value can be 
# found by combining the first digit and the last digit (in that order) 
# to form a single two-digit number.
# What is the sum of all of the calibration values?

def solve_01(data):    
    sum = 0
    firstdigit = re.compile(r"^.*?([0-9]).*")
    lastdigit = re.compile(r".*([0-9]).*?$")
    for str in data:
        s1 = firstdigit.fullmatch(str)
        s2 = lastdigit.fullmatch(str)
        
        if s1 is not None and s2 is not None:            
            sum += int(s1[1] + s2[1])
            
    return sum

# Your calculation isn't quite right. It looks like some of the digits
# are actually spelled out with letters: one, two, three, four, five, 
# six, seven, eight, and nine also count as valid "digits".
def solve_01b(data):
    sum = 0
    textdigits = [None,"one","two","three","four","five","six","seven","eight","nine"]
    firstdigit = re.compile(r"^.*?([0-9]|one|two|three|four|five|six|seven|eight|nine).*")
    lastdigit = re.compile(r".*([0-9]|one|two|three|four|five|six|seven|eight|nine).*?$")
    for str in data:
        s1 = firstdigit.fullmatch(str).expand(r"\1")
        s2 = lastdigit.fullmatch(str).expand(r"\1")

        if s1 is not None and s2 is not None:            
            tens = textdigits.index(s1) if s1 in textdigits else int(s1)
            ones = textdigits.index(s2) if s2 in textdigits else int(s2)
        
            sum += 10 * tens + ones
            
    return sum


if __name__ == '__main__':
    data = util.getInput("../inputs/01.txt")

    print(solve_01(data))
    print(solve_01b(data))