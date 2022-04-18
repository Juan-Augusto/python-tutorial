from math import hypot

first_side = float(input("Enter the length of the first side: "))
second_side = float(input("Enter the length of the second side: "))
print("The length of the hypotenuse is {}".format(hypot(first_side, second_side)))