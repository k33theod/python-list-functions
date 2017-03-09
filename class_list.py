from pprint import pprint as pp
from copy import deepcopy
from functools import reduce

class ML(list):
	
	def shape(self):
		bathos=0
		for i in str(self):
			if i!='[':
				break
			bathos+=1
		_shape=[]
		while bathos>0:
			_shape.append(len(self))
			self=self[0]
			bathos-=1
		return _shape
	
	def flatten(self):
			c=''.join([i for i in str(self)if i not in'[] ']).strip(',')
			return super(list(map(int,c.split(','))))
	
	def rows_to_columns(self):
		b=list(zip(*self))
		return super([list(i) for i in b])
	
	def items(self):
		return reduce(lambda x,y :x*y, ML.shape(self)) 
		

def create_list(val, *dimensions):
	dimensions = list(dimensions)
	if len(dimensions):
		current = dimensions.pop()
	else:  # finished!
		return val
	next_list = []
	for i in range(current):
		next_list.append(deepcopy(val))
	return create_list(next_list, *dimensions)
	 
