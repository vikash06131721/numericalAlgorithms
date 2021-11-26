
import numpy as np 
import cupy as cp
from cupy.linalg import det
from cupy.linalg import inv

class numerical_basics():

    def __init__(self,device):
        self.device =device

    def matrix_mult(self, matrix1,matrix2):
        """
        The matrix multiplication is perhaps the basic of Linear algebra. 
        A simple rule which must be observed is that the number columns of Mat1 should be equal
        to number of rows Mat2.

        matrix1 = numpy array
        matrix2 = numpy array
        """
        cp.cuda.Device(self.device).use()
        
        if matrix1.shape[1]==matrix2.shape[0]:
            matrix1 = cp.array(matrix1)
            matrix2 = cp.array(matrix2)
            return matrix1.dot(matrix2)
        else:
            print ("matrix multiplication not possible as 'matrix1' columns is not same as rows of\
            'matrix2'")
            return None

    def cross_prod(self,v,w):
        """
        The cross product between two vectors, v and w, is written v×w. 
        It is defined by v×w=∥v∥2∥w∥2sin(θ)n, where θ is the angle between the 
        v and w (which can be computed from the dot product) and n is a vector 
        perpendicular to both v and w with unit length (i.e., the length is one). 
        The geometric interpretation of the cross product is a vector perpendicular 
        to both v and w with length equal to the area
        enclosed by the parallelogram created by the two vectors.
        """
        cp.cuda.Device(self.device).use()
        if len(v)==len(w):
            v = cp.array(v)
            w = cp.array(w)
            return cp.cross(v, w)
        else:
            print ("Non equal in length vectors, cross product not possible")
            return None
    
    def calc_determinant(self,matrix1):
        """
        A square matrix is an n×n matrix; that is, it has the same number of rows as columns. 
        The determinant is an important property of square matrices and is scalar in nature 
        The determinant is denoted by det(M)
        matrix1 = numpy array
        """
        cp.cuda.Device(self.device).use()
        if matrix1.shape[0]==matrix1.shape[1]:
            matrix1 = cp.array(matrix1)
            return det(matrix1)
        else:
            print ("The matrix is non-square")
            return None

    def calc_inverse(self,matrix1):
        """
        The inverse of a square matrix M is a matrix of the same size, N, such that M⋅N=I.
        To find the inverse of the matrix the determinat should be non-zero
        """
        cp.cuda.Device(self.device).use()
        matrix1 = cp.array(matrix1)

        return inv(matrix1)

    
