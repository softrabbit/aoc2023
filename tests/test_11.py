import sys
sys.path.append("..")

from solutions import solution_11

data = ["...#......",
".......#..",
"#.........",
"..........",
"......#...",
".#........",
".........#",
"..........",
".......#..",
"#...#....."]


def test_11():
    assert solution_11.solve_11(data) == 374
    
def test_11b():    
    assert solution_11.solve_11b(data, 10) == 1030
    assert solution_11.solve_11b(data, 100) == 8410

