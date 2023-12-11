import sys
sys.path.append("..")

from aoclib import util

# Find the single giant loop starting at S. How many steps along the loop
# does it take to get from the starting position to the point farthest 
# from the starting position?
def solve_10(data):
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

    # S is the starting position of the animal; there is a pipe on this tile, 
    # but your sketch doesn't show what shape the pipe has.
    for y0 in range(0,len(data)):                   
        if -1 != (x0 := data[y0].find('S')):
            break
    print(x0,y0)

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
                print(f"{x} {y} {cx} {cy} {comefrom} {pipe}")
                if not path or direction != path[-1]:             
                    # Let's not go if we're doing a 180
                    path.append(comefrom)                    
                    (x,y) = (cx,cy)
                    print(f"OK {x} {y}")

            if (x,y) == (x0,y0) and path:
                loop = False
                break

    return len(path)/2

# Oh, but how many tiles are inside the loop?
def solve_10b(data):
    # Great. How do I define "outside" and "inside"?
    return None

if __name__ == '__main__':
    data = util.getInput("../inputs/10.txt")
    print( solve_10(data) )

