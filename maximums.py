# Replace the "ANSWER HERE" for your answer

def max_of_two(x, y):
    """Given x and y, that are 2 numbers, return the biggest number."""
    if x >= y:
        biggest = x
    else:
        biggest = y
    return biggest

def max_of_three(x, y, z):
    """Given x, y and z, that are 3 numbers, return the biggest number of the three."""
    if x >= y and x >= z:
        biggest = x
    elif y >= x and y >= z:
        biggest = y
    else:
        biggest = z
    return biggest
