import sys
sys.path.append("..")

from solutions import solution_06

data = ["Time:      7  15   30", "Distance:  9  40  200"]

def test_06():
    assert solution_06.solve_06(data) == 288

def test_06b():
    assert solution_06.solve_06b(data) == 71503