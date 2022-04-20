main_value = int(input("Enter a number between 1 and 9999: "))
if main_value > 9999 or main_value < 1:
    print("Invalid input")
else:
    to_string = str(main_value)
    print("units: {}".format(to_string[-1]))
    print("tens: {}".format(to_string[-2]))
    print("hundreds: {}".format(to_string[-3]))
    print("thousands: {}".format(to_string[-4]))

