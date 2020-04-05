'''
Test for the Filters
'''

import fiters as ft
import numpy as np
from  PIL import  Image
import matplotlib.pyplot as plt

A = np.array([[1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [6, 7, 8, 9, 10]])
B = np.array([[1,1,-1], [1,2,3], [1,2,4]])
C = ft.Imfilter(A, B)
print(C)
'''
a= 5
b= 5
A = np.array([[1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [6, 7, 8, 9, 10]])
[c ,d ]= A.shape
C= np.zeros(A.shape)
print(C, c, d)
'''