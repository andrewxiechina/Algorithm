# Vector

A python implementation of vector.
```python
from math import sqrt

class Vector:
  def __init__(self, arr):
      self.values = arr;
      
  def add(self, v):
      assert v != None
      assert len(self.values) == len(v.values)
      r = v._copy();
      for i in range(len(v.values)):
          r.values[i] += self.values[i];
          
      return r;
  
  def _copy(self):
      values = self.values[:]; #Copy a list
      return Vector(values);
      
  def equals(self, v):
      for i in range(len(v.values)):
          if self.values[i] != v.values[i]:
              return False;
      return True;     
      
  def __str__(self):
      s = "(";
      for i in range(len(self.values)):
          if i != 0: s += ","
          s += str(self.values[i]);
      s += ")";
      return s;
      
  def subtract(self, v):
      assert v != None
      assert len(self.values) == len(v.values)
      r = v._copy();
      for i in range(len(v.values)):
          r.values[i] = self.values[i] - r.values[i];
          
      return r;
  
  def dot(self, v):
      assert v != None
      assert len(self.values) == len(v.values)
      r = v._copy();
      for i in range(len(v.values)):
          r.values[i] = self.values[i] * r.values[i];
          
      sum = 0;
      for i in range(len(r.values)):
          sum += r.values[i];
      return sum;
      
  def norm(self):
      sum = 0;
      for i in range(len(self.values)):
          sum += self.values[i]*self.values[i];
      return sqrt(sum);
```
