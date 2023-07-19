import numpy as np
from generating_Possible_orientations import *
import copy
from datetime import datetime

def print_time():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S.%f")
    print("Current Time =", current_time)




def disregrad_wrapping(position, adjacent):
    #checks if cells are adjacent spacially as well as in terms of numerical position
    border_checks = ((position % 4 == 0 and adjacent == -1), 
    (position % 4 == 3 and adjacent == 1),
    (position % 16 < 4 and adjacent == -4),
    (position % 16 > 11 and adjacent == 4))

    return any(border_checks)

def check_any_zeroes_surrounded(cube):
    '''
    Given a matrix, returns True if any zero in the matrix 
    has only non-zero elements adjacent in the x,y or z plane (diagonals not considered)
    This checks if it is impossible to fill a space for collection of pieces
    '''
    for position, value in enumerate(cube.flatten()):
        if value == 0:
            adjacent_values = []
            for adjacent_cell in [1, 4, 16, -1, -4, -16]:
                if (0 <= position + adjacent_cell < 64) and not disregrad_wrapping(position, adjacent_cell):
                    adjacent_values.append(cube.flatten()[position + adjacent_cell])
            if all(adjacent_values):
                return True
    return False

print_time()




'''
Each layerX_orientations list is a list of 8 pieces. Each piece is a list of matrices that represent all the possible positional and rotational derivatives of the pieces within
the 4x4x4 grid.
layer1_orientations contains derivatives that must have unit cubes in the first layer
layer_2_orientations contains derivatives with no cubes in the first layer, and must have cubes in the second layer
layer_3_orientations contains derivatives with no cubes in the first or second  layer, and must have cubes in the third layer
layer_4_orientations contains derivatives with cubes in only the 4th layer

Nesting; layer_orientations[layer][piece][derivative]
'''
layer1_orientations = [[orientation for orientation in possible_orientations_flat[current_piece] if orientation[0,:,:].max() == 1] for current_piece in range(len(pieces))]
layer2_orientations = [[orientation for orientation in possible_orientations_flat[current_piece] if orientation[1,:,:].max() == 1 and orientation[0,:,:].max() == 0] for current_piece in range(len(pieces))]
layer3_orientations = [[orientation for orientation in possible_orientations_flat[current_piece] if orientation[2,:,:].max() == 1 and orientation[0:2,:,:].max() == 0] for current_piece in range(len(pieces))]
layer4_orientations = [[orientation for orientation in possible_orientations_flat[current_piece] if orientation[3,:,:].max() == 1 and orientation[0:3,:,:].max() == 0] for current_piece in range(len(pieces))]

layer_orientations = [layer1_orientations, layer2_orientations, layer3_orientations, layer4_orientations]




available_pieces = list(range(0, len(pieces))) #Index of available pieces
cube = np.zeros((4,4,4)) # generate a unfilled 4x4x4 space as our starting point
solution_pieces = []



print('Start backtracking')
print_time()

def backtrack(cube, available_pieces, solution_pieces):
    '''
    Recursive backtracking algorithm that progressively fills layers in the 4x4x4 space
    Algorithm palces a piece 
    '''
    iteration_available_pieces = copy.copy(available_pieces) #Copy to stop mutation in place down the recursion tree
    current_piece = iteration_available_pieces.pop(0) 
    for layer in range(4):
        if scan_layer(layer, cube, iteration_available_pieces, current_piece, solution_pieces):
            return 

def scan_layer(layer, cube, iteration_available_pieces, current_piece, solution_pieces):
    if cube[layer,:,:].min() == 0:
        for piece_position in layer_orientations[layer][current_piece]: #Iterate through the list of piece positions for the current layer
            iteration_solution_pieces = copy.copy(solution_pieces)
            iteration_solution_pieces.append(piece_position)
            iteration_cube = copy.copy(cube)
            iteration_cube = iteration_cube + piece_position
            if len(iteration_available_pieces) < 7:
                if iteration_cube.max() == 1 and not check_any_zeroes_surrounded(cube):
                    if len(iteration_available_pieces) == 0:
                        print('Solution found!')
                        for number, piece in enumerate(iteration_solution_pieces):
                                print('Piece number ' + str(number+1) + 'in position ' + str(piece))
                        print_time()
                        exit()

                    else:
                        backtrack(iteration_cube, iteration_available_pieces, iteration_solution_pieces)

            else:
                backtrack(iteration_cube, iteration_available_pieces, iteration_solution_pieces)

print(backtrack(cube, available_pieces, solution_pieces))

print_time()