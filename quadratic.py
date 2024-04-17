import math
# Replace the "ANSWER HERE" for your answer


def roots(a, b, c):
    radicando = math.pow(b, 2) - 4 * a * c
    if radicando > 0:
        x1 = (-b + math.sqrt(radicando)) / (2 * a)
        x2 = (-b - math.sqrt(radicando)) / (2 * a)
        return f"({x1}, {x2})"
    if radicando == 0:
        # Tiene 1 raiz doble
        x = (-b + math.sqrt(radicando)) / (2 * a)
        return f"({x})"
    else:
        # No tiene raices
        return "( )"


def value_y(a, b, c, x):
    return (a * math.pow(x, 2)) + (b * x) + c


def to_string(a, b, c):
    quadratic = ""
    linear = ""
    if a != 0:
        quadratic = f" {a} * X^2 +"
    if b != 0:
        linear = f" {b} * X +"
    return f"f(x) ={quadratic}{linear} {c}"


def derivation(a, b, c):
    quadratic = ""
    linear = ""
    if a != 0:
        quadratic = f" {2*a} * X"
        if b != 0:
            quadratic += " +"
            linear = f" {b}"
    else:
        linear = f" {b}"
    return f"f'(x) ={quadratic}{linear}"
