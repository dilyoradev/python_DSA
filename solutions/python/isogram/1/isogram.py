def is_isogram(string):
    lower_string = string.lower()
    new_isogram = []
    for char in lower_string:
        if char == " " or char == "-":
            continue
        if "a" <= char <= "z":
            if char in new_isogram:
                return False
            else:
                new_isogram.append(char)
    return True
            
            
