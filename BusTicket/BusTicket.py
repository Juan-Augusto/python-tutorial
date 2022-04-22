distance_traveled = int((input("Enter the distance traveled in km: ")))

if distance_traveled < 200:
    print('The price of the ticket is USD {}'.format(distance_traveled * 0.5))
else:
    print('The price of the ticket is USD {}'.format(distance_traveled * 0.45))