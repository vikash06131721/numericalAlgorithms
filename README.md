# numericalAlgorithms
A repository and a package for implementation of numerical analysis based on GPU

# Basic Functions
from numericalPython.basic_functions import numerical_basics

basics = numerical_basics(device=5)
basics.matrix_mult(matrix1,matrix2)

basics.cross_prod(v,w)

basics.calc_determinant(matrix1)


Configurable arguments:

1. device : device id
2. matrix, v, w: numpy arrays

## Installation
1. git clone https://github.com/vikash06131721 numericalAlgorithms.git

2. cd numericalAlgorithms/

3. python setup.py install

## License
MIT



