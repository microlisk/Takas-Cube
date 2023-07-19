import numpy as np


'''
The finished cube can be thought of as a 4x4x4 grid of 64 unit cubes. Each piece has physical dimensions that align with this grid
Each piece can be represented as occupying specific spaces within a 3x3x3
Pieces are represented initially in list or array format with a top down view, 0 representing empty space, 1 representing presence of a unit cube. 
2 represents 2 unit cubes stacked on top of each other, as viewed from above i.e the depth of the piece.
'''

p1 = [2,2,0,
      2,2,2,
      2,2,2]

p2 = [2,2,2,
      2,0,0,
      2,0,0]

p3 = [1,1,0,
      1,1,1,
      1,1,1]

p4 = [2,2,2,
      2,0,0,
      0,0,0]

p5 = [0,0,1,
      1,1,1,
      1,1,1]

p6 = [2,2,0,
      2,0,0,
      0,0,0]

p7 = [1,1,1,
      1,0,0,
      1,0,0]

p8 = [1,1,1,
      1,0,0,
      0,0,0]



pieces = [p1,p2,p3,p4,p5,p6,p7,p8]
pieces_str = ['p1','p2','p3','p4','p5','p6','p7','p8']

pieces_dict = {pieces_str[i]:pieces[i] for i in range(len(pieces))}

two_dimensional_arrays_dict = {pieces_str[i]:np.asarray(pieces[i]).reshape(3,3) for i in range(len(pieces))}







