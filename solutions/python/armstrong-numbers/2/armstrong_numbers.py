"""functions that judge whether the put-in number is an armstrong number"""
def is_armstrong_number(number):
    digit = str(number)
    power = len(digit)
    return sum(int(digit) ** power for digit in str(number)) == number
