import sys
sys.path.append("..")

from solutions import solution_08

data1 = r"""RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)
"""

data2 = r"""LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)
"""

data3 = r"""LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)
"""

def test_08():
    assert solution_08.solve_08(data1.splitlines()) == 2
    assert solution_08.solve_08(data2.splitlines()) == 6

def test08b():
    assert solution_08.solve_08b(data3) == 6

