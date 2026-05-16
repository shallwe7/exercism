"""Functions for calculating grains on a chessboard."""

def square(number):
    """calculate the grain number of the specific number of square"""
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")
    return 2 ** (number - 1)
    

def total():
    """calculate the total number of the grain on the chess"""
    return sum(square(number_i) for number_i in range(1, 65))
