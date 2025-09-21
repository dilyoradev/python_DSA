def score(x, y):
    unit = ((x*x) + (y*y)) ** 0.5
    if unit <= 1:
        points = 10
    elif unit <= 5:
        points = 5
    elif unit <= 10:
        points = 1

    else:
        points = 0
    return points
    
