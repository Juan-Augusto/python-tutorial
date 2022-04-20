phrase = input("Enter a phrase: ")

print("The letter A appears {} times in the phrase".format(phrase.upper().count("A")))
print("The letter A appears in the position {} for the first time".format(phrase.upper().find("A") + 1))
print("The letter A appears in the position {} for the last time".format(phrase.upper().rfind("A") + 1))

