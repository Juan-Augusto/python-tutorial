side_storage = []
for i in range (3):
    num = int(input("enter the size of the triangle side: "))
    side_storage.append(num)
if side_storage[0] < side_storage[1] + side_storage[2] and side_storage[1] < side_storage[0] + side_storage[2] and side_storage[2] < side_storage[0] + side_storage[1]:
    print("This is a triangle")
    print('The sides of the triangle are: {}'.format(side_storage))
    print('The perimeter of the triangle is: {}'.format(side_storage[0] + side_storage[1] + side_storage[2]))
else:
    print("This is not a triangle")

