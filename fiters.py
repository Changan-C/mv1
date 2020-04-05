import numpy as np
from pylab import *
from PIL import Image

def prewittx(X):
    A = array([1,0,-1],[1,0,-1],[1,0,-1])
    print(A)
    return A
##A = array([[1,0,-1],[1,0,-1],[1,0,-1]])
##print(A)
def Imfilter(A,B):
    '''
    :param A:Image Matrix
    :param B:Filter Matrix
    :return:the Image after filter
    '''
    i = 0
    j = 0
    [row, con] = np.shape(A)
    [c,d] = np.shape(B)
    t = int((c-1)/2)
    r = int((d-1)/2)
    New_A = np.zeros(A.shape)
    for i in range(row):
        for j in range(con):
            New_A[i,j] =0
            a = i-t
            b = j-r
            for a in range(c):
                for b in range(d):
                    if a < 0 or b < 0:
                        New_A[i, j] = New_A[i,j] + 0 * B[a+t-i, b+r-j]
                    else:
                        New_A[i, j] = New_A[i, j] + A[a, b] * B[a + t - i, b + r - j]
    return New_A
