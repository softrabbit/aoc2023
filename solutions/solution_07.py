import sys
sys.path.append("..")

from aoclib import util
from functools import cmp_to_key


# Return how many of a kind there are
def handtype(h, b=False):
    if b:
        # Make sure the jokers get sorted first
        h = h.replace('J','*')
    h = sorted(h)

    # Figure out which is the first non-joker card
    firstcard = 0
    tmp = ''.join(h)
    
    if tmp.startswith("****"):
        firstcard = 4
    elif tmp.startswith("***"):
        firstcard = 3
    elif tmp.startswith("**"):
        firstcard = 2
    elif tmp.startswith("*"):
        firstcard = 1

    if h[firstcard] == h[4]:
        # Five of a kind, if all cards are the same (also handles 5 jokers case)
        return 5
    elif h[firstcard] == h[3] or h[1] == h[4]:
        # Four
        return 4
    elif h[0] == h[1] and h[3] == h[4] and h[2] in [h[1], h[3]]:
        # Full house
        return 3.5
    elif firstcard == 1 and h[1] == h[2] and h[3] == h[4]:
        return 3.5
    elif h[0] == h[2] or h[2] == h[4] or h[1] == h[3]:
        # Three
        return 3 if firstcard == 0 else 4
    else:
        # Here we only can have pairs left, I hope
        pairs = 0
        for n in range(firstcard,4):
            if h[n] == h[n+1]:
                pairs += 1
        # 2: two pairs, 1: one pair, 0: high card
        if pairs == 1:
            return firstcard + 2 if firstcard > 0 else 1 # 1-3 jokers plus the pair
        if pairs == 0:
            if firstcard == 1: # 1 joker makes a pair
                pairs = 1
            if firstcard == 2: # 2 make 3 of a kind
                pairs = 3
            return pairs

        if pairs == 0 and firstcard == 1:
            pairs = 1 # Can't have more than one joker at this point, right?
        return pairs
    # Should never happen
    return 0

def handstrength(h1, h2, b=False):    
    if b:
        cardorder = "AKQT98765432J"
    else:
        cardorder = "AKQJT98765432"

    if handtype(h1,b) == handtype(h2,b):
        # Cardwise comparison
        for n in range(0,5):
            x = cardorder.find(h1[n]) - cardorder.find(h2[n])            
            if x != 0:                
                return x
               
    return handtype(h2,b) - handtype(h1,b)

def handcompare_a(h1,h2):
    return handstrength(h1,h2,False)

def handcompare_b(h1,h2):
    return handstrength(h1,h2,True)


def solve_07(data,b):
    hands = {}
    for line in data:
        hand, bid = line.split()
        hands[hand] = int(bid)
    
    sortfunc = handcompare_b if b else handcompare_a
    # Sort function goes from strongest, so reverse
    keylist = list(reversed(sorted(hands, key=cmp_to_key(sortfunc))) )
    
    rank = 0
    sum = 0
    for k in keylist:
        rank += 1
        sum += rank * hands[k]                 
    return sum

def solve_07b(data):
    return solve_07(data,True)
    
if __name__ == '__main__':
    data = util.getInput("../inputs/07.txt")
    print( solve_07(data) )
    print( solve_07b(data) )

