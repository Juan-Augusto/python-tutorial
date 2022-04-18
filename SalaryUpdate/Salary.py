from codecs import IncrementalDecoder


current_salary = float(input('What is your current salary? '))
increase_percentage = float(input('What percentage do you want to increase your salary? '))
print('Your salary will be {}'.format(current_salary + (current_salary * increase_percentage / 100)))
