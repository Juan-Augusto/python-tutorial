wall_length = int(input("Enter the length of the wall: "))
wall_height = int(input("Enter the height of the wall: "))
paint_coverage = float(input("How many square meters can a liter paint cover? "))
print("The area of the wall is {} square meters".format(wall_length * wall_height))
print("The amount of paint needed is {} liters".format(wall_length * wall_height / paint_coverage))
