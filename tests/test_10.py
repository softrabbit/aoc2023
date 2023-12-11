import sys
sys.path.append("..")

from solutions import solution_10
from aoclib import util

data1 = [".....",".S-7.",".|.|.",".L-J.","....."]
data2 = ["..F7.",".FJ|.","SJ.L7","|F--J","LJ..."]

data3 = ["...........",
    ".S-------7.",
    ".|F-----7|.",
    ".||OOOOO||.",
    ".||OOOOO||.",
    ".|L-7OF-J|.",
    ".|II|O|II|.",
    ".L--JOL--J.",
    ".....O....."]

data4 = [".F----7F7F7F7F-7....",
    ".|F--7||||||||FJ....",
    ".||.FJ||||||||L7....",
    "FJL7L7LJLJ||LJ.L-7..",
    "L--J.L7...LJS7F-7L7.",
    "....F-J..F7FJ|L7L7L7",
    "....L7.F7||L7|.L7L7|",
    ".....|FJLJ|FJ|F7|.LJ",
    "....FJL-7.||.||||...",
    "....L---J.LJ.LJLJ..."]

def test_10():
    # First part
    assert solution_10.solve_10(data1) == 4
    assert solution_10.solve_10(data2) == 8
    
def test_10b():
    assert solution_10.solve_10b(data3) == 4
    assert solution_10.solve_10b(data4) == 8