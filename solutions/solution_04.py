import sys
sys.path.append("..")

from aoclib import util
import re
import functools

# Picking one up, it looks like each card has two lists of numbers 
# separated by a vertical bar (|): a list of winning numbers and then a 
# list of numbers you have. You organize the information into a table 
# (your puzzle input).
# As far as the Elf has been able to figure out, you have to figure out
# which of the numbers you have appear in the list of winning numbers.
# The first match makes the card worth one point and each match after 
# the first doubles the point value of that card.

# Take a seat in the large pile of colorful cards. How many points are 
# they worth in total?

def solve_04(data):
    cardformat = re.compile(r"^Card\s+(\d+):(.*)\|(.*)$")
    sum = 0
    for card in data:
        parts = cardformat.match(card)
        winners = set(parts[2].split())
        hand = set(parts[3].split())
        count = len(winners & hand)        
        
        sum += 2**(count-1) if count > 0 else 0

    return sum


# There's no such thing as "points". Instead, scratchcards only cause you
# to win more scratchcards equal to the number of winning numbers you have.
# Specifically, you win copies of the scratchcards below the winning card 
# equal to the number of matches. So, if card 10 were to have 5 matching 
# numbers, you would win one copy each of cards 11, 12, 13, 14, and 15.
# Including the original set of scratchcards, how many total scratchcards 
# do you end up with?
def solve_04b(data):
    cardformat = re.compile(r"^Card\s+(\d+):(.*)\|(.*)$")    
    cardinfo = {}
    # I know I'm overcomplicating it, but I want to play around with some 
    # data structures like tuples
    for card in data:
        parts = cardformat.match(card)
        cardnum = int(parts[1])
        winners = set(parts[2].split())
        hand = set(parts[3].split())
        details = winners, hand, 1 # Count of this card
        cardinfo[cardnum] = details

    cardnums = sorted(cardinfo.keys())
    for cursor in cardnums:
        winners, hand, count = cardinfo[cursor]
        wins = len(winners & hand) 
        if wins > 0:
            for n in range(1,wins+1):
                if (cursor + n) in cardnums:
                    # Oh, tuples are immutable...
                    t1, t2, t3 = cardinfo[cursor+n]
                    cardinfo[cursor+n] = (t1,t2, t3+count)
                    
    # NB The 0 at the end is needed to force the result into an int
    return functools.reduce(lambda sum,card: sum + card[2], cardinfo.values(), 0 )    

    return None


if __name__ == '__main__':
    data = util.getInput("../inputs/04.txt")
    print( solve_04(data) )
    print( solve_04b(data) )
