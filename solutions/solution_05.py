import sys
sys.path.append("..")

from aoclib import util
import re
import functools

# - Which seeds need to be planted (header "Seeds")
# - A list of maps which describe how to convert numbers from a source
#   category into numbers in a destination category.
# - The maps describe entire ranges of numbers that can be converted. 
#   Each line within a map contains three numbers: the destination
#   range start, the source range start, and the range length.
# - Any source numbers that aren't mapped correspond to the same 
#   destination number. 

# What is the lowest location number that corresponds to any of the 
# initial seed numbers?

# Parsing common to both parts of the assignment.
# Returns a tuple with all the needed data, which is: 
# - a list of seed numbers
# - a dictionary: { (from_tag, to_tag): [ (to, range(from, len) ) ...], (from, to): [ ] }

def parse_05(data):
    seeds = None
    mapfrom = None
    mapto = None
    maps = {}

    mapidpattern = re.compile(r"^([a-z]+)-to-([a-z]+) map:$")
    maplinepattern = re.compile(r"^([0-9]+)\s+([0-9]+)\s+([0-9]+)$")    
    for line in data:        
        # First comes a line with the seed numbers (skip empty if need be)
        if line.startswith("seeds: "):
            seeds = list(map(int, line[6:].split()))
        elif m := mapidpattern.fullmatch(line.strip()):
            mapfrom = m[1]
            mapto = m[2]
            maps[(mapfrom,mapto)] = []
        elif m := maplinepattern.fullmatch(line.strip()):
            # Order of map data: to, from, length            
            maps[(mapfrom, mapto)].append( (int(m[1]), range(int(m[2]), int(m[2]) + int(m[3])) ) )
    
    return (seeds,maps)

def solve_05(data, b=False):
    seeds, maps = parse_05(data)
    # A quick solution for the second part, except it'll run for a long time and
    # eat all available memory and then some if you feed it the actual input.
    if b:
        tmp = []
        for n in range(0,len(seeds),2):
            tmp.extend(range(seeds[n], seeds[n]+seeds[n+1]))
        seeds = tmp
        
    # Start with the "seed" category, if the input is correct only one map will fit
    tag = "seed"
    while tag != "location":
        # Find the map mapping from "tag" to the next category
        for k in maps.keys():
            if k[0] == tag:
                mapranges = maps[k]
                next = k[1]

        tmp = []
        for x in seeds:
            appended = False
            for m in mapranges:
                if x in m[1]:
                    tmp.append(x-m[1][0] + m[0])
                    appended = True
            if not appended:
                tmp.append(x)
        seeds = tmp
        tag = next

    return min(seeds)


# Split r1 if it overlaps r2 and return (left,overlap,right),
# None if no overlap
def split_overlap(r1,r2):
    if r1.start > r2.stop-1 or r2.start > r1.stop-1:
        return None
    return (range(r1.start, r2.start) if r1.start < r2.start else None,
        range(max(r1.start,r2.start), min(r1.stop,r2.stop)),
        range(r2.stop, r1.stop) if r1.stop > r2.stop else None)

# The values on the initial seeds: line come in pairs. 
# Within each pair, the first value is the start of the range 
# and the second value is the length of the range.
def solve_05b(data):    
    seeds, maps = parse_05(data)    
    seedranges = []
    for n in range(0,len(seeds),2):
        seedranges.append(range(seeds[n], seeds[n]+seeds[n+1]))
    
    tag = "seed"
    while tag != "location":
        # Find the map mapping from "tag" to the next category
        for k in maps.keys():
            if k[0] == tag:
                mapranges = maps[k]
                next = k[1]

        tmp = []
        for r in seedranges:
            appended = False
            for m in mapranges:
                ovr = split_overlap(r, m[1])
                if ovr is not None:
                    # We should have a tuple
                    (left, mid, right) = ovr                                        
                    if left is not None:
                        # Put the ends back for checking against mappings.
                        # Thank Guido that Python supports adding to the
                        # array you're looping over
                        seedranges.append(left)
                    if right is not None:
                        seedranges.append(right)
                    # Map the middle part
                    m0 = mid.start - m[1].start + m[0]
                    tmp.append(range(m0, m0+len(mid)))
                    appended = True
            if not appended:
                # didn't fit any of the mappings
                tmp.append(r)
        seedranges = tmp        
        tag = next

    return min(map(lambda r: r.start, seedranges ) )


if __name__ == '__main__':
    data = util.getInput("../inputs/05.txt")
    print( solve_05(data) )
    print( solve_05b(data) )

