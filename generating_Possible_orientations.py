from three_dimensional_pieces import *
from generating_positions import *
from generating_symmetry import *


'''
We are generating a nested list, where each element is a piece, and each piece is a list of roataional/postional derivative matrices for that piece
possible_oreitnations[piece][rotational_derivative][position]
possible_orientations_flat[piece][derivative]
'''

_rotational_derivatives = []
for piece in three_d_arrays_dict.values():
    _rotational_derivatives.append(generate_rotational_derivatives(piece))


_rotational_derivatives[0] = [three_d_arrays_dict['p1']]
_possible_orientations = []


for piece in _rotational_derivatives:
    piece_positions = []
    for derivative in piece:
        generated_positions = generate_all_positions_recursive(derivative, [derivative])
        piece_positions.append(generated_positions)
    _possible_orientations.append(piece_positions)
 



possible_orientations_flat = [[item for sublist in piece for item in sublist]for piece in _possible_orientations]


