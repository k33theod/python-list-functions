class multi_list(list):
	def get_shape(self):
		bathos=0
		for i in str(self):
			if i!='[':
				break
			bathos+=1
		shape=[]
		while bathos>0:
			shape.append(len(self))
			self=self[0]
			bathos-=1
		return shape
    
		def flatten_list(self):
      c=''.join([i for i in str(self)if i not in'[] ']).strip(',')
      return multi_list(list(map(int,c.split(','))))
  
  
  
from copy import deepcopy
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
	 
