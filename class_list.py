class multi_list(list):
  def __init__(self,lista):
    self=lista
  def get_shape(self):
    """
    Returns the shape of the multidimensional array of numbers a
    """
    self.bathos=0;
    for i in str(self):
      if i!='[':
        break
      self.bathos+=1
    self.shape=[]
    while bathos>0:
      self.shape.append(len(self))
      self=self[0]
      self.bathos-=1
    return self.shape 
