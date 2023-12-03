import sys
sys.path.append("..")

from solutions import solution_01

def test_01():
    data = ["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"]
    assert solution_01.solve_01(data) == 142
    
def test_01b():
    data = ["two1nine","eightwothree","abcone2threexyz","xtwone3four","4nineeightseven2","zoneight234","7pqrstsixteen"]
    assert solution_01.solve_01b(data) == 281

