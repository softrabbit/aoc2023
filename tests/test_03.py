from solutions import solution_03



data= [ "467..114..",
        "...*......",
        "..35..633.",
        "......#...",
        "617*......",
        ".....+.58.",
        "..592.....",
        "......755.",
        "...$.*....",
        ".664.598.." ]

def test_03():        
    assert solution_03.solve_03(data) == 4361
    
def test_03b():        
    assert solution_03.solve_03b(data) == 467835
