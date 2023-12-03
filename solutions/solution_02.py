import sys
sys.path.append("..")

from aoclib import util
from lark import Lark, Transformer, v_args


# Determine which games would have been possible if the bag had been 
# loaded with only 12 red cubes, 13 green cubes, and 14 blue cubes. 
# What is the sum of the IDs of those games?
@v_args(inline=True)
class GameTransformer(Transformer):
    def color_count(self, items, what):
        print(items)
        return "CC"

    def game_id(self, items):
        print(items)
        return "GI"
        

def solve_02(data):
    cubes = {"red": 12, "green": 13, "blue": 14}    
    # Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
    grammar = r"""
        start: game_id ":" reveals
        game_id: "Game" id -> game_id
        id: NUMBER
        reveals: reveal ";" reveals | reveal
        reveal: color_count | color_count "," reveal
        color_count: count COLOR -> color_count
        count: NUMBER
        COLOR: "red"|"green"|"blue"

        TEXT: /[a-z]+/

        %import common.NUMBER
        %import common.WS
        %ignore WS
        
"""
    parser = Lark(grammar, parser="lalr", transformer=GameTransformer())
    for line in data:
        # print(line)
        print(parser.parse(line))                

    return 0


if __name__ == '__main__':
    data = util.getInput("../inputs/02.txt")
    print( solve_02(data) )
