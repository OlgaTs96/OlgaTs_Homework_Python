import math


def square(side):
    return math.ceil(side * side)


side = input("Введите длину стороны: ")

s = float(side)

print(square(s))
