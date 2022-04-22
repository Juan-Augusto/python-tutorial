car_speed = int(input("Please enter the speed of the car: "))

if car_speed > 80:
    print("You are driving too fast, your ticket will be USD {}".format((car_speed - 80) * 7))
else:
    print("You are driving at a safe speed")