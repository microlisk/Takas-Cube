from define_pieces import *
import numpy as np

'''
Convert the 2D represenation into a 3D array, with 0 indicating empty space and 1 indicating a unit cube in this space
'''

#Convert the dictionary of lists do dictionary of 2-d arrays
two_dimensional_arrays_dict = {pieces_str[i]:np.asarray(pieces[i]).reshape(3,3) for i in range(len(pieces))}


def two_dim_to_3_dim(array):
    if 2 in array:
        stacked_planes = np.dstack((array, array))
        three_d_array = np.dstack((np.zeros((3,3,1)), stacked_planes))
        three_d_array[three_d_array !=0] = 1
        return three_d_array

    else:
        return np.dstack((np.zeros((3,3,2)), array))
    
def reshape_3x3_to4x4(array):
    array3x3x4 = np.dstack((np.zeros((3,3,1)), array))
    array4x3x4 = np.vstack((np.zeros((1,3,4)), array3x3x4))
    array4x4x4 = np.hstack((np.zeros((4,1,4)), array4x3x4))
    #Rearranging axis zero to depth, pieces are now 'flat' when viewed from axis zero
    return np.swapaxes(array4x4x4, 0,2)

def piece_4x4x4_representation(array):
    return reshape_3x3_to4x4(two_dim_to_3_dim(array))
    


three_x_three_piece_dict = {pieces_str[i]:two_dim_to_3_dim(list(two_dimensional_arrays_dict.values())[i]) for i in range(len(pieces)) }
three_d_arrays_dict = {pieces_str[i]:piece_4x4x4_representation(list(two_dimensional_arrays_dict.values())[i]) for i in range(len(pieces)) }   



