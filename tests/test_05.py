import sys
sys.path.append("..")

from solutions import solution_05
from aoclib import util

data = util.getInput("tests/test_05.txt")

def test_05():
    assert solution_05.solve_05(data) == 35
    
def test_05b():    
    assert solution_05.solve_05b(data) == 46
    