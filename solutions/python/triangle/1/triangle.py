def equilateral(sides):
    if len(sides) != 3:
        return False
    a, b, c = sides
    if a > 0 and b > 0 and c > 0 and a + b >= c and b + c >= a and a + c >= b:
        return a == b == c
    return False

def isosceles(sides):
    if len(sides) != 3:
        return False
    a, b, c = sides
    if a > 0 and b > 0 and c > 0 and a + b >= c and b + c >= a and a + c >= b:
        return a == b or a==c or b== c
    return False



def scalene(sides):
    if len(sides) != 3:
        return False
    a, b, c = sides
    if a > 0 and b > 0 and c > 0 and a + b >= c and b + c >= a and a + c >= b:
        return a != b and b != c and a != c
    return False
