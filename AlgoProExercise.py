# 3
print(f'A Shinigami [verb] my adjective [noun] out of the [noun2] as\
if he were a vegetarian fishing a [noun3] out of his salad.')

verb = input("Enter a verb: ")
adjective = input("Enter an adjective: ")
noun = input("Enter a noun: ")
noun2 = input("Enter a second noun: ")
noun3 = input("Enter a third noun: ")

print(f'A Shinigami {verb} my {adjective} {noun} out of the {noun2} as\
if he were a vegetarian fishing a {noun3} out of his salad.')

# 2
m, F = float(input("Enter the mass (kg): ")), float(input("Enter the force (N): "))
a = F/m
print("The acceleration is: " + str(a))

# 1
print("Enter your height.")
feet = int(input("Feet: "))
inches = int(input("Inches: "))
T_inches = feet * 12 + inches
height_cm = T_inches * 2.54
board_length = height_cm * 0.88
print(f'Suggested board length: {board_length}')
