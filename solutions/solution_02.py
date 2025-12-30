import sys
sys.path.append("..")

from aoclib import util
from lark import Lark, Transformer, v_args

# Cubes in the bag
cubes = {"red": 12, "green": 13, "blue": 14}    

# Determine which games would have been possible if the bag had been 
# loaded with only 12 red cubes, 13 green cubes, and 14 blue cubes. 
# What is the sum of the IDs of those games?
@v_args(inline=True)
class GameTransformer(Transformer):    
    def start(self, id, possible):
        return({"game_id": id, "possible": possible})

    def game_id(self, id):        
        return id
        
    def id(self, id):        
        return int(id)

    # All the reveals in one game must be True
    def reveals(self,*items):
        b = True
        for i in items:
            b = b and i
        #print(items)
        return b


    # Returns true if all colors pulled less than maximum
    def reveal(self,*items):
        b = True
        for i in items:
            b = b and i
        #print(b)
        return b

    # Returns true if colors pulled less than maximum
    def color_count(self, count, what):
        #print(str(items) + " " + str(what))
        return count <= cubes[what] 

    def count(self, num):
        return int(num)

    def COLOR(self,items):
        return str(items)

    

def solve_02(data):    
    # Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
    grammar = r"""
        start: game_id ":" reveals
        game_id: "Game" id -> game_id
        id: NUMBER
        reveals: reveal ";" reveals | reveal
        reveal: color_count+
        color_count: count COLOR | "," count COLOR -> color_count
        count: NUMBER        
        COLOR: "red"|"green"|"blue"

        TEXT: /[a-z]+/

        %import common.NUMBER
        %import common.WS
        %ignore WS
        
"""
    parser = Lark(grammar, strict=True, parser="lalr", transformer=GameTransformer())
    sum = 0
    for line in data:
        #print(line)
        res = parser.parse(line)
        print(res)
        if res["possible"]:
            sum += int(res["game_id"])
        
    return sum


if __name__ == '__main__':
    data = util.getInput("../inputs/02.txt")
    print( solve_02(data) )
