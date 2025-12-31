import sys
sys.path.append("..")

from aoclib import util
from lark import Lark, Transformer, v_args
import time
import array 

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
# Slow first implementation. Will need better.
def solve_08b_1(data):
    directions, graph = build_graph(data)
    positions = list(filter(lambda k: k.endswith("A"), graph.keys() ))
    counter = 0
    done = False
    z = 0 
    t0 = time.time()
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
        z += 1
        if z % 10000 == 0:
            print(10000/(time.time() - t0 ))
            t0 = time.time()
    return counter

# Maybe up to ~15% more loops/sec than the first one - made directions an 
# array of ints and graph a dict of 2-element arrays + some more squeezing
def solve_08b(data):
    _directions, _graph = build_graph(data)
    positions = list(filter(lambda k: k.endswith("A"), _graph.keys() ))
    # Sets are faster than lists
    endpositions = set(filter(lambda k: k.endswith("Z"), _graph.keys() ))
    
    # Swap out the strings for numbers
    #directions = array.array('I') # which type is fastest?
    directions = [] # List seems to win over array.array
    for d in _directions:
        directions.append(0 if d=="L" else 1)
    
    graph = {}
    for k,v in _graph.items():
        graph[k] = [v["L"], v["R"]]
    counter = 0
    done = False
    z = 0 
    t0 = time.time()
    # Precalculating this speeds the innermost loop a little,
    # surprisingly unrolling it by 2 seems to slow it?
    pos_idxs = range(len(positions))
    print(endpositions)
    while not done:
        for direction in directions:            
            done = True
            for n in pos_idxs: 
                # Step all positions and check if all end with Z
                # Temporary avoids list subscripts
                tmp = graph[positions[n]][direction]
                positions[n] = tmp
                done = done and (tmp in endpositions)            
            #done = sorted(positions) == endpositions # Not good - slow!
            counter += 1            
            if done:
                break
        z += 1
        if z % 10000 == 0:
            print(10000/(time.time() - t0 ))
            t0 = time.time()
    return counter
# Ideas for speed:
# - Try spreading this to multiple threads (one for each path)
# - Compiled language? OpenCL/C(++)/Rust ?
# - Smarter algorihthm, for each path:
#    - find out if the path starts looping i.e. ends up twice at the
#      same end state with an identical phase of the direction array?
#    - is there a period before the loop starts?

if __name__ == '__main__':
    data = util.getInput("../inputs/08.txt")
    #print( time.time() )
    #print( solve_08(data) )
    #print( time.time() )
    print( solve_08b(data) )
