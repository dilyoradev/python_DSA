def square(number):
    if 64 < number or number < 1:
        raise ValueError("square must be between 1 and 64")
    return 2 ** (number-1)
        

def total():
    return sum(square(number) for number in range(1,65))
