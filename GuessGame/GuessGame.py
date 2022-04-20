from random import randint


main_number = int(input("Enter a number between 1 and 5: "))
computer_number = randint(1, 5)
print('Computer says: {}'.format(computer_number))
if main_number == computer_number:
    print("You guessed it!")
else:
    print("You didn't guess it!")