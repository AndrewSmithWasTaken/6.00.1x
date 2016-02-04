def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    t = a
    while a%t != 0 or b%t != 0:
        t -= 1
    return t