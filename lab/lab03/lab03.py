""" Lab 3: Recursion and Midterm Review """

def gcd(a, b):
    """Returns the greatest common divisor of a and b.
    Should be implemented using recursion.

    >>> gcd(34, 19)
    1
    >>> gcd(39, 91)
    13
    >>> gcd(20, 30)
    10
    >>> gcd(40, 40)
    40
    """
    "*** YOUR CODE HERE ***"
    larger = max(a,b) 
    smaller = min(a,b) 
    if larger % smaller == 0:
        return smaller
    else:
        return gcd(smaller,larger % smaller)

step = 0
def hailstone(n):
    """Print out the hailstone sequence starting at n, and return the
    number of elements in the sequence.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    "*** YOUR CODE HERE ***"
    global step
    step += 1
    print(n)
    if n == 1:
        return step
    elif n % 2 == 0:
        return hailstone(n//2)
    else:
        return hailstone(n*3+1)
