import sys
sys.path.append("..")

from solutions import solution_09
from aoclib import util

data = ["0 3 6 9 12 15",
        "1 3 6 10 15 21",
        "10 13 16 21 30 45"]

def test_09():
    # First part
    assert solution_09.solve_09(data, solution_09.Edge.right) == 114
    # Second part
    assert solution_09.solve_09(data, solution_09.Edge.left) == 2