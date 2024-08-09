from math import sqrt
first_side_length = input("Enter length of first side:")
second_side_length = input("Enter length of second side:")
first_side_length = int(first_side_length)
second_side_length = int(second_side_length)
hypotenuse = sqrt((first_side_length**2) + (second_side_length**2))
hypotenuse = round(hypotenuse, 2)
print("The length of the hypotenuse is {}".format(hypotenuse))