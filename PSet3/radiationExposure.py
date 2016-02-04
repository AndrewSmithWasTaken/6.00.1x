def radiationExposure(start, stop, step):
    '''
    Computes and returns the amount of radiation exposed
    to between the start and stop times. Calls the 
    function f (defined for you in the grading script)
    to obtain the value of the function at any point.
 
    start: integer, the time at which exposure begins
    stop: integer, the time at which exposure ends
    step: float, the width of each rectangle. You can assume that
      the step size will always partition the space evenly.

    returns: float, the amount of radiation exposed to 
      between start and stop times.
    '''  
    def myRange(x, y, step):
        while x < y:
            yield x
            x += step
    exp = 0.0
    totalExp = 0.0  
    for x in myRange(start, stop, step):
        exp = (f(x) * step)
        totalExp += exp
    return totalExp

#>>> radiationExposure(0, 5, 1)
#39.10318784326239

#>>> radiationExposure(0, 4, 0.25)
#1148.6783342153556

#def f(x):
#    import math
#    return 10*math.e**(math.log(0.5)/5.27 * x)

    
    
    