iterations = int(input("Enter the number of iterations: "))
number_storage = []
print('Write {} numbers:'.format(iterations))
for i in range (iterations):
    num = int(input("enter a number: "))
    number_storage.append(num)
print('The numbers you entered are: {}'.format(number_storage))
print('The lowest number you entered is: {}'.format(min(number_storage)))
print('The greatest number you entered is: {}'.format(max(number_storage)))

