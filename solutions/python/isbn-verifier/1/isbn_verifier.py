def is_valid(isbn):
    clean_isbn = isbn.replace("-", "")
    if len(clean_isbn) != 10:
        return False
    total = 0
    for i, num in enumerate(clean_isbn):
        if num == "X":
            if i != 9:
                return False
            value = 10
        elif num.isdigit():
            value = int(num)
        else:
            return False
        weight = 10 - i
        total += value * weight

    return total % 11 == 0
