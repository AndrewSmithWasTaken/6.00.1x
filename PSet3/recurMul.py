def recurMul(a,b):
    if b == 1:
        return a
    else:
        return a + recurMul(a, b-1)
        
r = recurMul(2,3)
print r