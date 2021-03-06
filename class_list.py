from copy import deepcopy

class ML(list):
	
	def reshape(self,*dimesions):
    		self=self.flatten()
    		return self._reshape(*dimesions)
  	
	def _reshape(self,*dimesions):
    		dimesions=list(dimesions)
    		mul=1
    		for i in dimesions:
      			mul*=i
    		if mul!=len(self):
      			raise (ValueError)("The product of dimensions should me equal to {}".format(len(self)))
    		if len(dimesions)>1:
      			current = dimesions.pop()
    		else:  # finished!
      			return type(self)(self)
    		result=[]
    		index=0
    		while index<len(self) :
      			result.append(list(self[index:index+current]))
      			index+=current
    		return type(self)._reshape(result,*dimesions)	
  	
	@property
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
    		return type(self)(list(map(int,c.split(','))))

  	def rows_to_columns(self):
    		b=list(zip(*self))
    		return type(self)([list(i) for i in b])
	
	@property
  	def items(self):
    		self=self.flatten()
    		return len(self) 
    	
	@classmethod
	def create_list(cls, val, *dimensions):
    		dimensions = list(dimensions)
    		if len(dimensions):
      			current = dimensions.pop()
    		else:  # finished!
      			return cls(val)
    		next_list = []
    		for i in range(current):
      			next_list.append(deepcopy(val))
    		return cls.create_list(next_list, *dimensions)
