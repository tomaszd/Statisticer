#import numpy

from numpy  import *
print 'This is how numpy will be usefull '

a = arange(15).reshape(3, 5)
print a
print 'a.shape',a.shape
print 'a.ndim',a.ndim
print 'a.dtype.name',a.dtype.name
print 'a.itemsize',a.itemsize
print 'a.size',a.size
print 'type(a)',type(a)
b = array([6, 7, 8])
array([6, 7, 8])
type(b)
print 'result of arrays'    
result_of_arrays=a*3
print 'result_of_arrays=a*5',result_of_arrays
arangA=arange(10,30,5)
print 'arange(10,30,5)',arangA
arangA=arange(1,2,0.12)
print 'arange(1,2,0.12)',arangA
table_to_rotate=arange(12).reshape(4,3)
print table_to_rotate
print rot90(table_to_rotate)
