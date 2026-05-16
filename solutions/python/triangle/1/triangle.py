"""Moudele that provides functions about defining triangles"""


def is_valid(sides):
    """Function that verify whether it is a triangle"""
    a, b, c = sides
    return a > 0 and b > 0 and c > 0 and a + b >= c and b + c >= a and a + c >= b

def equilateral(sides):
    """Function that verify equilateral"""
    a, b, c = sides
    return is_valid(sides) and a == b == c 

def isosceles(sides):
    """Function that verify isosceles"""
    a, b, c = sides
    return is_valid(sides) and (a == b or a == c or b == c) 


def scalene(sides):
    """Function that verify scalene"""
    return is_valid(sides) and not isosceles(sides)
