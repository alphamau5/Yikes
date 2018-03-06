'''
Here is an n-dimensional vector class.

This class can compute vector-scalar multiplication, the inner product of 
two vectors, addition of vectors, and multiple combinations.

Purpose:
- create a custom type (Vector) and manipulate a Python class successfully
- implement operators for classes such as __init__ and __setitem__
- combine Python fundamentals with exceptions to ensure proper input
'''

class Vector:
    
    def __init__(self, l):
        
        self.l = l
        
        if type(self.l) != list:
            raise TypeError
        
        for c in self.l:
            if type(c) == int or type(c) == float:
                pass
            else:
                raise TypeError
    
    def dim(self):
        return len(self.l)
    
    def __getitem__(self, i):
        if i < 1 or i > self.dim():
            raise IndexError
        else:
            return self.l[i-1]
   
    def __setitem__(self, i, x):   
        if i < 1 or i > self.dim():
            raise IndexError
        else:
            self.l[i-1] = x
      
    def __mul__(self, other):
        
        if type(other) == Vector:
            if other.dim() == self.dim():
                x = []
                u = 0
                while u < self.dim():
                    x.append(self.l[u]*other.l[u])
                    u+=1
                return sum(x)
                #dot product
                
            else: #not the same dimension, raise an error
                raise ValueError
        else: 
            pass
          
        if type(other) == int or type(other) == float:
            x = []
            u = 0
            while u < self.dim():
                x.append(self.l[u]*other)
                u+=1
            x=Vector(x)
            return x
        else:
            raise AssertionError
    
    def __rmul__(self, other):        
    
        if type(other) == Vector:
            if other.dim() == self.dim():
                x = []
                u = 0
                while u < self.dim():
                    x.append(other.l[u]*self.l[u])
                    u+=1
                return sum(x)
                
            else:
                raise ValueError
        else: 
            pass
                
        if type(other) == int or type(other) == float:
            x = []
            u = 0
            while u < self.dim():
                x.append(other*self.l[u])
                u+=1
            x=Vector(x)
            return x
        else:
            raise AssertionError
         
    def __add__(self, other):    
    
        if type(other) != Vector or other.dim() != self.dim():
            raise ValueError
        else:
            z = []
            u = 0
            while u < self.dim():
                z.append(self.l[u]+other.l[u])
                u+=1
            z=Vector(z)
            return z
        
    def __str__(self):
        return 'Vector: ' + str(self.l)
