from three_dimensional_pieces import *
from generating_positions import *
import numpy as np

def _piece_move_available(array):
    '''
    Return max of the first column, row, array. We use this to check if we need
    to move the piece towards the bottom left corner 
    '''
    filled_layers = array[0,:,:].max()
    filled_rows = array[:,0,:].max()
    filled_columns = array[:,:,0].max()

    return [filled_layers, filled_rows, filled_columns]


def _move_to_bottom_left_corner(derivatives):
    '''
    Move the piece to the bottom left corner of the grid
    '''
    for index, derivative in enumerate(derivatives):
        available_planes = _piece_move_available(derivative)
        for axis, plane in enumerate(available_planes):
            if plane == 0:
                derivative = np.roll(derivative, -1, axis=axis)
                derivatives[index] = derivative
                _move_to_bottom_left_corner(derivatives)


def generate_rotational_derivatives(piece):
    '''
    Function generates all 24 possible rotations in an octahedral space;
    Gives us all possible way to place a cube where the cube is placed in line with axes
    '''
    derivatives = []

    #Generate a rotation so that we have a view of each face
    face2 = np.rot90(piece, k=1, axes=(0,1))
    face3 = np.rot90(piece, k=2, axes=(0,1))
    face4 = np.rot90(piece, k=3, axes=(0,1))
    face5 = np.rot90(piece, k=1, axes=(0,2))
    face6 = np.rot90(piece, k=3, axes=(0,2))
    faces = [piece, face2, face3, face4, face5, face6]

    # Then rotate the piece 90 degrees 1, 2 and 3 times about axis 0
    for face in faces:
        derivatives.append(face)
        for z_rotation in range(1,4):
            derivatives.append(np.rot90(face, k=z_rotation, axes=(1,2)))

    # Function moves all derivatives to bottom left corner
    #move_to_bottom_left_corner(derivatives)
                
    return derivatives

