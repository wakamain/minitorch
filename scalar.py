# import math and numpy for matrix calculation (Linear Algebra)
import math
import numpy as np

# typing for better type annotation
from typing import Union, Sequence, Tuple

# Scalar Class (An object that contains a singular value e.g an int or float)
# A scalar is a single number that represents a quantity, having magnitude but no direction.
class Scalar:
  def __init__(self, value):
    self.value = value

  # https://docs.python.org/3/library/functions.html#repr
  def __repr__(self):
    return f"{self.value}"
  
  # Addition
  def __add__(self, other):
    other = other if isinstance(other, Scalar) else Scalar(other)
    return Scalar(self.value + other.value)
  
  # Negation
  def __neg__(self):
    return self * -1
  
  # Subtraction
  def __sub__(self, other):
    return self + (-other)
  
  # Multiplication
  def __mul__(self, other):
    other = other if isinstance(other, Scalar) else Scalar(other)
    return Scalar(self.value * other.value)
  
  # Exponentiation
  def __pow__(self, other):
    if isinstance(other, Scalar):
      other = other.value
    return Scalar(self.value**other)
    
  # Divsion
  def __truediv__(self, other):
    return self * other**-1
  
A = Scalar(1)
B = Scalar(2)
C = A + 5
D = B - 9.0
E = A * 74
F = B / 9*5
G = B / (9*5)
print(C)
print(D)
print(E)
print(F)
print(G)