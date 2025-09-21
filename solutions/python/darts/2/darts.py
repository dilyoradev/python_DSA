def score(x, y):
    unit = ((x*x) + (y*y)) ** 0.5
    if unit <= 1:
        return 10
    elif unit <= 5:
        return 5
    elif unit <= 10:
        return 1
    else:
        return 0
    
