import sys
sys.path.append("..")

from aoclib import util
from lark import Lark, Transformer, v_args

# AAA = (BBB, CCC)
grammar = r"""
start: NODECODE "=" "(" NODECODE "," NODECODE ")"
NODECODE: /[A-Z0-9]{3}/

%import common.WS
%ignore WS
"""

@v_args(inline=True)
class GraphTransformer(Transformer):    
    def start(self, name, left, right):
        return({"node": str(name), "outs": {"L": str(left), "R": str(right)}})

    def NODECODE(self, item):
        return str(item)

def build_graph(data):
    parser = Lark(grammar, strict=True, parser="lalr", transformer=GraphTransformer())    
    graph = {}
    directions = data[0].strip()
    for line in data[2:]:
        #print(line)
        tmp = parser.parse(line)
        graph[tmp["node"]] = tmp["outs"]
    return directions, graph


# Traverse a graph and return the number of steps from AAA to ZZZ
def solve_08(data):
    directions, graph = build_graph(data)
    position = "AAA"
    counter = 0
    while position != "ZZZ":
        for direction in directions:            
            position = graph[position][direction]
            #print(f"{direction} -> {position}")
            counter += 1
            if position == "ZZZ":
                break
            
    return counter

# Traverse in parallel from every **A node until 
# all paths are on **Z nodes simultaneously
def solve_08b(data):
    directions, graph = build_graph(data)
    positions = list(filter(lambda k: k.endswith("A"), graph.keys() ))
    counter = 0
    done = False
    while not done:
        for direction in directions:            
            done = True
            for n in range(len(positions)):
                # Step all positions and check if all end with Z
                positions[n] = graph[positions[n]][direction]
                done = done and positions[n].endswith("Z")
            counter += 1            
            if done:
                break
            
    return counter
    

if __name__ == '__main__':
    data = util.getInput("../inputs/08.txt")
    print( solve_08(data) )
    print( solve_08b(data) )
