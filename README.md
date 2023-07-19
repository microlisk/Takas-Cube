# Code for solving Taka's Cube

### Files are;
* define_pieces_py ; Define the pieces as 2-D arrays
* three-dimensional_pieces.py ; Convert to 3-D array representation
* generating_positions.py ; Functions to generate all positional derivatives for a piece
* generating_symmetry.py ; Functions for generating all rotational derivatives of a piece
* generating_Possible_orientations.py ; Apply above functions to generate all positional/rotational derivatives for all piece
* backtracking_layers.py ; Backtracking script to find solution using possible orientations 
* solution.py ; the solution as numpy matrices
* Vectary.com 3D-Model.zip ; puzzle modelled using vectary.com; can import this file(unzipped) on vectary.com to manipulate the model
