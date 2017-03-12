# python-list-functions
An extension to class list 
A number of methods and properties that extend the list class

PROPERTIES

.shape
returns in a list the shape of object
mylist.shape 
[3,4,5,2] means there are 3 sublists each of them has 4 sumblists each has 5 sublists each of them has 2 elements

.items
returns the number of items of the object
mylist.items
12
12 means if we make the list flat the length is 12

METHODS

.flatten()
mylist.flatten()
returns a flat list

.rows_to_columns()
mylist.rows_to_columns()
from a 2 dimensional list returns another 2 dimensional where columns are ther rows of object and columns the rows
if mylist.shape is [3,4] we get a [4,3] shape list

cls.create_list(a,*dimensions)
Is a class lever method
ML.create_list(1,2,3,4)
The first argument is the value of all elemenst of the list the next are the shape of the list

.reshape(shape)
returns a list with the given shape
mylist.reshape(*shape)
returns a list with the given shape
