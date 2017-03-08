def grammes_stiles(a):
  b=list(zip(*a))
  return [list(i) for i in b]


def flatten_list(a):
  """
  Returns a one dimension list from the multidimensional list of numbers a
  """
  c=''.join([i for i in str(a)if i not in'[] ']).strip(',')
  return list(map(int,c.split(',')))

def check_balance(a):
	stack=[]
	maches={'(':')', '[':']', '{':'}'}
	for i in a: 
		if i in maches:
			stack.append(i)
		elif i in maches.values():
			if (not stack) or maches[stack[-1]]!=i:
				return False
			stack.pop()
	return not stack  

a=[[[2,3],[12,78],[11,2],[1,0]],[[7,2],[3,2],[7,5],[4,2]],[[4,1],[2,1],[78,0],[45,12]],[[12,3],[3,7],[5,6],[12,8]],[[4,5],[6,2],[1,0],[5,6]]]  

def get_shape(a):
  """
  Returns the shape of the multidimensional array of numbers a
  """
  bathos=0;
  for i in str(a):
    if i!='[':
      break
    bathos+=1
  shape=[]
  while bathos>0:
    shape.append(len(a))
    a=a[0]
    bathos-=1
  return shape
  
  
from functools import reduce
def get_items(a):
  """
  Returns the number of items of the multidimensional array of numbers a
  """
  return reduce(lambda x,y :x*y, get_shape(a)) 


def create_list(ind,*b):
	"(contend of list, 1st list dimension, \
	[other list dimensions])--> n dimennsions list  \
	n must be 1-6"
	a=len(b) #list dimensions
	d=1 #a pointer that grows to the list dimensions (a)
	while True:
		pinakas=[ind]*b[0] # 1 dimension list 
		d+=1 # increase the pointer
		if d>a: break #control if pointer is larger to dimensions if not continous
		for i in range(b[0]): # add a second dimension 
			pinakas[i]=[ind]*b[1]
		d+=1
		if d>a: break
		for i in range(b[0]):	
			for j in range(b[1]):
				pinakas[i][j]=[ind]*b[2]
		d+=1
		if d>a: break		
		for i in range(b[0]):	
			for j in range(b[1]):
				for k in range(b[2]):
					pinakas[i][j][k]=[ind]*b[3]
		d+=1
		if d>a: break
		for i in range(b[0]):	
			for j in range(b[1]):
				for k in range(b[2]):
					for l in range(b[3]):
						pinakas[i][j][k][l]=[ind]*b[4]
		d+=1
		if d>a: break
		for i in range(b[0]):	
			for j in range(b[1]):
				for k in range(b[2]):
					for l in range(b[3]):
						for m in range(b[4]):					
							pinakas[i][j][k][l]=[ind]*b[5]
		d+=1
		if d>a: break
	return pinakas  

  
  
def reshape_list(a,*args):
  komatia=reduce(lambda x,y :x*y, args[:-1])
  bathos=len(args)-1
  my_list = flatten_list(a)
  idex=0
  new_list=create_list(1,*args[:-1])
  kommati=get_items(a)/args[-1]
  while bathos>0:
    for i in new_list:
  
  new_list.append(my_list[idex:idex+kommati])
  idex+=kommati
       
    bathos-=1
    idex+=1  
  return my_list
  return komatia,bathos

def reshape_array(a,*args):
  komatia=reduce(lambda x,y :x*y, args[:-1])
  my_list = flatten_list(a)
  index=0
  new_list=create_list(1,b,c)
  for i in len(b)
  
  shape=get_shape(a)
  bathos=len(shape)
  
  for i in len(shape[0]):
    for j in len(shape[1]):
      for k in len (shape[2]):
        a[i][j][k]=2
  



  
A = [None] * 3 
for i in range(3):
    A[i] = [None] * 2
