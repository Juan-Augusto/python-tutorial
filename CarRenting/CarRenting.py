traveled_distance = int(input("Enter the distance traveled in km: "))
days_rented = int(input("Enter the number of days rented: "))
print("The cost of the rental is {}".format(traveled_distance * 0.15 + days_rented * 60))