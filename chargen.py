from random import randint

def rollstat():
    """
    returns an int as the sum of the top 3 rolls of 5d6
    """
    rolls = [randint(1,6) for i in range(5)]
    rolls.sort()
    return sum(rolls[2::])

def getstats():
    """
    Returns list of 6 rolled stats
    """
    return [rollstat() for stat in range(6)]
