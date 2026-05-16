"""Moudele that provides functions about defining triangles"""


def is_valid(sides):
    """Function that verify whether it is a triangle"""
    a_side, b_side, c_side = sides
    return a_side > 0 and b_side > 0 and c_side > 0 and a_side + b_side >= c_side and b_side + c_side >= a_side and a_side + c_side >= b_side

def equilateral(sides):
    """Function that verify equilateral"""
    a_side, b_side, c_side = sides
    return is_valid(sides) and a_side == b_side == c_side 

def isosceles(sides):
    """Function that verify isosceles"""
    a_side, b_side, c_side = sides
    return is_valid(sides) and (a_side == b_side or a_side == c_side or b_side == c_side) 


def scalene(sides):
    """Function that verify scalene"""
    return is_valid(sides) and not isosceles(sides)
