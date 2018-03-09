'''
The valid function takes a function (f) and a list (l) and
returns what items in l are valid for a given f.
'''
import math

def valid(f, l):
    
    try:
        for i in l:
            f(i)
    except:
        del(l[l.index(i)])
        valid(f,l)
        
    return l
    
'''
examples:

valid(chr, [-1, 10, 123.456, 2**20]) == [10]
valid(asin, [0.3, -0.1, -1, 1, 'sneezing panda', '1', 1.3]) == [0.3, -0.1, -1, 1]
valid(sqrt, [-3, -0.1, 0, 8]) == [0, 8]
'''
