# import math and numpy for matrix calculation (Linear Algebra)
import math
import numpy as np

# typing for better type annotation
from typing import Union, Sequence, Tuple

# Scalar Class (An object that contains a value e.g an int or float)
class Scalar:
  def __init__(self, value):
    self.value = value

  def __repr__(self):
    return f"{self.value}"

A = Scalar(1.0)
print(A)