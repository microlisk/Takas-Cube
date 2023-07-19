from three_dimensional_pieces import *
import numpy as np



def piece_move_available(array):
    '''
    Returns three lists of n elements each. Each list give us the max value for each layer, row and column in an nxnxn array.
    Give us empty/non-empty planes if our array is encoding 1 as a filled cell and 0 as empty
    '''
    occupied_layers = [array[i,:,:].max() for i in range(4)]
    occupied_rows = [array[:,i,:].max() for i in range(4)]
    occupied_columns = [array[:,:,i].max() for i in range(4)]

    return [occupied_layers, occupied_rows, occupied_columns]


def generate_all_positions_recursive(array, possible_positions):
    '''
    First checks for empty planes at the edge of an nxnxn array
    Then rolls array towards empty edge
    Recursively applies itself to the rolled array, generating all possible positions a shape can fill in an nxnxn array
    without chaning orientation of the shape
    '''                                    
    for axis in range(3):
        if piece_move_available(array)[axis][0] == 0:
            copy = np.roll(array, -1, axis=axis)
            if not any([np.array_equal(copy, position) for position in possible_positions]):
                possible_positions.append(copy)
                for axis in range(3):
                    if any([piece_move_available(copy)[axis][i]==0 for i in range(3)]):
                        generate_all_positions_recursive(copy, possible_positions)

        if piece_move_available(array)[axis][-1] == 0:
            copy = np.roll(array, 1, axis=axis)
            if not any([np.array_equal(copy, position) for position in possible_positions]):
                possible_positions.append(copy)
                for axis in range(3):
                    if any([piece_move_available(copy)[axis][i]==0 for i in range(3)]):
                        generate_all_positions_recursive(copy, possible_positions)
          
    return possible_positions



 
    





        




