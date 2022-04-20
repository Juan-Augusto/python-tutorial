full_name = input("Enter your full name: ")

print("Your name is {}".format(full_name.upper()))
print("Your name is {}".format(full_name.lower()))
print("Theres {} letters in your name".format(len(full_name) - full_name.count(" ")))
print("Your first name has {} letters".format(len(full_name.split()[0]))) # split() returns a list of strings