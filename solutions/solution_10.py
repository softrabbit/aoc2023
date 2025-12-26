import sys
sys.path.append("..")

from aoclib import util

# N, E, S, W mappings (clockwise!)
pipes = {'|':  [True, False, True, False],
        '-':  [False, True, False, True],
        'L':  [True, True, False, False],
        'J':  [True, False, False, True],
        '7':  [False, False, True, True],
        'F':  [False, True, True, False],
        '.':  [False, False, False, False], # ground; there is no pipe in this tile.
        'S':  [True, True, True, True]      # Start, should be able to enter from all directions?            
}
# vectors for N, E, S, W
nswe = [(0,-1), (1,0), (0,1), (-1,0) ]

# Find the single giant loop starting at S and return it.
def find_loop(data):
    # S is the starting position of the animal; there is a pipe on this tile, 
    # but your sketch doesn't show what shape the pipe has.
    for y0 in range(0,len(data)):                   
        if -1 != (x0 := data[y0].find('S')):
            break
    #print(x0,y0)

    x = x0
    y = y0
    path = [] # stores the path

    loop = True
    while loop:
        for direction in range(0, len(nswe)):
            if not pipes[data[y][x]][direction]:
                continue
            # Get candidate position, I don't even pretend to 100% understand this
            (cx,cy) = tuple(sum(i) for i in zip ((x,y), nswe[direction]) )
            
            # Edge cases
            if cx < 0 or cx >=len(data[0]) or cy < 0 or cy >=len(data):
                continue
                
            comefrom = (direction + 2) % len(nswe)
            pipe = data[cy][cx]
            if pipes[pipe][comefrom]: # We could go that way
                #print(f"{x} {y} {cx} {cy} {comefrom} {pipe}")
                if not path or direction != path[-1]:             
                    # Let's not go if we're doing a 180
                    path.append(comefrom)                    
                    (x,y) = (cx,cy)
                    #print(f"OK {x} {y}")

            if (x,y) == (x0,y0) and path:
                loop = False
                break

    return path

def solve_10(data):
    # How many steps along the loop
    # does it take to get from the starting position 
    # to the point farthest from the starting position?
    return len(find_loop(data))/2

# Oh, but how many tiles are enclosed by the loop?
def solve_10b(data):    
    path = find_loop(data)
    #print("\n".join(data))

    # First, copy only the looping path to a new map
    # Empty map with original dimensions
    newmap = []
    for row in data:
        newmap.append(" " * len(row) )

    # ...find starting point
    for y0 in range(0,len(data)):                   
        if -1 != (x0 := data[y0].find('S')):
            break
    # ...copy pipes on path to newmap
    x = x0 
    y = y0
    path.reverse() # Because we pushed the parts in reverse order
    for move in path:
        tmp = list(newmap[y])
        tmp[x] = data[y][x]
        newmap[y] = ''.join(tmp)

        x += nswe[move][0]
        y += nswe[move][1]
    #print("\n".join(newmap))

    # Correct pipe for starting position
    truth = [False, False, False, False]
    # North
    match newmap[y0-1][x0]: 
        case "|" | "F" | "7" :
            truth[0] = True
    # East       
    match newmap[y0][x0+1]:
        case "-" | "7" | "J":
            truth[1] = True
    # South 
    match newmap[y0+1][x0]: 
        case "|" | "J" | "L" :
            truth[2] = True
    # West       
    match newmap[y0][x0-1]:
        case "-" | "L" | "F":
            truth[3] = True
    S = None
    for k, bools in pipes.items():
        if truth == bools:
            S = k

    if S is None:
        print(f"Cant solve S: '{truth}'")
    tmp = list(newmap[y0])
    tmp[x0] = S
    newmap[y0] = ''.join(tmp)

    inside_tiles = 0
    # On every horisontal line, count tiles that are inside, i.e.
    # start at "out" and flip insideness on every crossing of boundary        
    # - vertical pipes are easy, straight flip, BUT
    # - corners on horizontal lines must be remembered, 
    #   i.e. F---7 won't change the insideness but F----J will
    for row in newmap:
        corner = None
        #print(f"{inside_tiles} {row}")
        inside = False
        for tile in list(row):
            match tile:
                case " ":
                    inside_tiles += 1 if inside else 0                        
                case "|":
                    inside = not inside
                case "F" | "L":
                    corner = tile
                case "7":
                    if corner == "L":
                        inside = not inside
                    corner = None
                case "J":
                    if corner == "F":
                        inside = not inside
                    corner = None

    return inside_tiles

if __name__ == '__main__':
    data = util.getInput("../inputs/10.txt")
    print( solve_10(data) )
    print( solve_10b(data) )

