
# Read a file, return lines. The most basic thing.
def getInput(filename):
    with open(filename) as f:
        data = list(map(str.strip, f.readlines()))

    return data