# import math and numpy for matrix calculation (Linear Algebra)
import math
import numpy as np

# typing for better type annotation
from typing import Union, Sequence, Tuple

# Scalar Class (An object that contains a singular value e.g an int or float)
# A scalar is a single number that represents a quantity, having magnitude but no direction.
class Scalar:
  def __init__(self, value, children=(), op=''):
    self.value = value
    self.grad = 0.0
    self._backward = lambda:None
    self.children = set(children)
    self.op = op

  # https://docs.python.org/3/library/functions.html#repr
  def __repr__(self):
    return f"{self.value}"
  
  # Addition
  def __add__(self, other):
    other = other if isinstance(other, Scalar) else Scalar(other)
    output = Scalar(self.value + other.value, children=(self, other), op='+')

    def _backward():
      self.grad += output.grad
      other.grad += output.grad

    output._backward = _backward
    return output
  
  # Negation
  def __neg__(self):
    return self * -1
  
  # Subtraction
  def __sub__(self, other):
    return self + (-other)
  
  # Multiplication
  def __mul__(self, other):
    other = other if isinstance(other, Scalar) else Scalar(other)
    return Scalar(self.value * other.value, children=(self, other), op='*')
  
  # Exponentiation
  def __pow__(self, other):
    if isinstance(other, Scalar):
      other = other.value
    return Scalar(self.value**other)
    
  # Divsion
  def __truediv__(self, other):
    return self * other**-1

  # Right hand operations (5 ◯ A)
  def __radd__(self, other):
    return self + other
  
  def __rsub__(self, other):
    return other + (-self)
  
  def __rmul__(self, other):
    return self * other
  
  def __rtruediv__(self, other):
    return other * self**-1
  
  def backward(self):
    topo = []
    visited = set()
    def build_topo(v):
      if v not in visited:
        visited.add(v)
        for child in v.children:
          build_topo(child)
        topo.append(v)
    build_topo(self)

    self.grad = 1.0
    for node in reversed(topo):
      node._backward()
  
A = Scalar(1)
B = Scalar(2)
C = A + B
print(f"A = {A}")
print(f"B = {B}")
print(f"A + B = {C}")
print("\n")
print(f"Gradient of A before calling .backward() = {A.grad}")
print(f"Gradient of B before calling .backward() = {B.grad}")
print("\n")
C.backward()
print(f"Gradient of A after calling .backward() = {A.grad}")
print(f"Gradient of B after calling .backward() = {B.grad}")
# I think the gradients should be 1 when adding since
# this indicates a proportional relationship between
# the input parameters A/B and the output C but am not sure