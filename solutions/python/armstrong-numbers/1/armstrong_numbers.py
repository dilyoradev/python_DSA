def is_armstrong_number(number):
    str_number = str(number)
    string_length = len(str_number)
    total = 0
    for num in str_number:
        total += int(num) ** string_length
    return total == number
        