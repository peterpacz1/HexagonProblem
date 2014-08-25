# Module imports
import math
import random

def randgen():
    """ Randomly generates numbers 1 through 6 in a random order """

    # Random order of numbers
    random_order = []

    # Generator
    while len(random_order) != 6:
        number = random.randrange(1, 7)

        # Checks for duplicate
        if number not in random_order:
            random_order.append(number)
    return random_order

def vertassign():
    """ Adds the random numbers from randgen() to the vertices dictionary """

    # Hexagon vertice matrix
    vertices = {
        1 : None,
        2 : None,
        3 : None,
        4 : None,
        5 : None,
        6 : None

    }
    # Initializes number cache
    numcache = randgen()

    # Iterates over vertices for number assignment
    for vertice in vertices:
        vertices[vertice] = numcache[0]

        # Remove assigned number from cache
        numcache.pop(0)
    return vertices

def multiplier():
    """ Multiplies each vertice sum with it's rightmost adjacent vertice """

    # Initialize assigned hexagon
    vertices = vertassign()

    # Pre-operation check
    for vertice in vertices:
        print vertices[vertice]

    # Main multiplication matrix
    segment1 = vertices[1] * vertices[2]
    segment2 = vertices[2] * vertices[3]
    segment3 = vertices[3] * vertices[4]
    segment4 = vertices[4] * vertices[5]
    segment5 = vertices[5] * vertices[6]
    segment6 = vertices[6] * vertices[1]

    # Returns total sum of all segment sums
    totalsum = segment1 + segment2 + segment3 + segment4 + segment5 + segment6
    return totalsum

def runner(attempts, permutations):
    """ Runs the program for a single execution loop"""
    # Calls multiplier for total sum (one of the answers)
    totalsum = multiplier()
    print "Sum %s permutation %s of %s attempts" % (totalsum, permutations, attempts)
    return totalsum

def statistics():
    """ Runs the program multiple times to determine the smallest sum """
    # Initialize the operation log
    log = []

    # Initialize statistic keeping daemons
    attempts = 0
    permutations = 0

    # Try for 1000 cycles
    while attempts != 1000:
        currentrun = runner(attempts, permutations)
        attempts = attempts + 1
        if currentrun not in log:
            log.append(currentrun)
            permutations = permutations + 1

    # Return answer
    answer = sorted(log)
    print "Program execution complete"
    print "We were able to discover"
    print "%s permutations from %s attempts" % (permutations, attempts)
    print "All permutations listed below from highest to lowest:"
    for score in answer:
        print score
    print "The smallest sum possible is %s" % (answer[0])
statistics()
