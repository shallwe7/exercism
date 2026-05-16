"""Module providing a function of leap year"""
def leap_year(year):
    """to test whether the year is leap year or not"""
    return (year % 100 == 0 and year % 400 == 0) or (year % 100 != 0 and year % 4 == 0)
