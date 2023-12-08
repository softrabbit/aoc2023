import sys
sys.path.append("..")

from aoclib import util
from functools import cmp_to_key

# Return how many of a kind there are
def handtype(h):
    h = sorted(h)
    if h[0] == h[4]:
        # Five of a kind
        return 5
    elif h[0] == h[3] or h[1] == h[4]:
        # Four
        return 4
    elif h[0] == h[1] and h[3] == h[4] and h[2] in [h[1], h[3]]:
        # Full house
        return 3.5
    elif h[0] == h[2] or h[2] == h[4] or h[1] == h[3]:
        # Three
        return 3
    else:
        pairs = 0
        for n in range(0,4):
            if h[n] == h[n+1]:
                pairs += 1
        # 2: two pairs, 1: one pair, 0: high card
        return pairs
    # Should never happen
    return 0

def cardwise(c1, c2):
    order = "AKQJT98765432"
    return order.find(c1) - order.find(c2)

def handstrength(h1, h2):
    if handtype(h1) == handtype(h2):
        # Cardwise comparison
        for n in range(0,4):
            x = cardwise(h1[n], h2[n])
            if x != 0:
                return x
            
    return handtype(h2) - handtype(h1)


def solve_07(data):
    hands = {}
    for line in data:
        hand, bid = line.split()
        hands[hand] = int(bid)
    
    # Sort function goes from strongest, so reverse
    keylist = list(reversed(sorted(hands, key=cmp_to_key(handstrength))) )
    
    rank = 0
    sum = 0
    prev = ""
    for k in keylist:
        if prev != k:
            # Identical hands get the same rank?
            rank += 1
        sum += rank * hands[k]
        print(f"{k}: {hands[k]} * {rank}")
        prev = k    
    return sum

if __name__ == '__main__':
    data = util.getInput("../inputs/07.txt")
    print( solve_07(data) )

