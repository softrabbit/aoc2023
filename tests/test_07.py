import sys
sys.path.append("..")

from solutions import solution_07

data = ["32T3K 765","T55J5 684","KK677 28","KTJJT 220","QQQJA 483"]

# Testcases from kind people on Reddit, these seem to work on part 1, but
# I still get failures on the real input...
data2 = ["AAAAA 2","22222 3","AAAAK 5","22223 7","AAAKK 11","22233 13",
    "AAAKQ 17","22234 19","AAKKQ 23","22334 29","AAKQJ 31","22345 37",
    "AKQJT 41","23456 43"]

data3 = ["2345A 2", "2345J 5", "J345A 3", "32T3K 7", "T55J5 17", "KK677 11",
    "KTJJT 23", "QQQJA 19", "JJJJJ 29", "JAAAA 37", "AAAAJ 43", "AAAAA 53",
    "2AAAA 13", "2JJJJ 41", "JJJJ2 31"]

def test_07(): 
    assert solution_07.solve_07(data, False) == 6440
    assert solution_07.solve_07(data2, False) == 1343
    assert solution_07.solve_07(data3, False) == 3542
    
def test_07b():
    # Tests while working out the joker logic
    assert solution_07.handtype("AAAAA", True) == 5    
    assert solution_07.handtype("AAJAA", True) == 5
    assert solution_07.handtype("AAJKJ", True) == 4
    assert solution_07.handtype("KTJJT", True) == 4    
    assert solution_07.handtype("AJJKJ", True) == 4
    assert solution_07.handtype("TTAAJ", True) == 3.5    
    assert solution_07.handtype("TAJKJ", True) == 3
    assert solution_07.handtype("AAJ89", True) == 3
    assert solution_07.handtype("AA8K8", True) == 2
    assert solution_07.handtype("A89KJ", True) == 1
    assert solution_07.handtype("A89K5", True) == 0
    assert solution_07.solve_07b(data) == 5905

