import sys
sys.path.append("..")

from aoclib import util
from lark import Lark, Transformer, v_args

# AAA = (BBB, CCC)
grammar = r"""
start: NODECODE "=" "(" NODECODE "," NODECODE ")"
NODECODE: /[A-Z]{3}/

%import common.WS
%ignore WS
"""

@v_args(inline=True)
class GraphTransformer(Transformer):    
    def start(self, name, left, right):
        return({"node": str(name), "outs": {"L": str(left), "R": str(right)}})

    def NODECODE(self, item):
        return str(item)


def solve_08(data):
    parser = Lark(grammar, strict=True, parser="lalr", transformer=GraphTransformer())
    directions = data[0].strip()
    map = {}
    for line in data[2:]:
        #print(line)
        tmp = parser.parse(line)
        map[tmp["node"]] = tmp["outs"]
    position = "AAA"
    counter = 0
    while position != "ZZZ":
        for direction in directions:            
            position = map[position][direction]
            #print(f"{direction} -> {position}")
            counter += 1
            if position == "ZZZ":
                break
            
    return counter


if __name__ == '__main__':
    data = util.getInput("../inputs/08.txt")
    print( solve_08(data) )

