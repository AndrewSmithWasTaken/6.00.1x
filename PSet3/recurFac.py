def recurFac(n):
    """assumes that n is an int > 0
        returns n!"""
    if n == 1:
        return n
    return n*recurFac(n-1)
    
r = recurFac(2,3)
print r