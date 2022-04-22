salary = int(input("Enter your salary: "))

if salary < 1250:
    print("Your new salary is {}".format(salary * 1.15))
else:
    print("Your new salary is {}".format(salary * 1.1))