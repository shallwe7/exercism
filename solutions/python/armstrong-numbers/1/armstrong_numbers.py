"""functions that judge whether the put-in number is an armstrong number"""
def is_armstrong_number(number):
    digit = str(number)
    power = len(digit)
    return sum(int(d) ** power for d in str(number)) == number
