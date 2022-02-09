firstVariable = '5';
secondVariable = int(firstVariable);
thirdVariable = str(secondVariable);
fourthVariable = float(secondVariable);
fifthVariable = int(fourthVariable);

print((firstVariable));
if isinstance(firstVariable, str):
    print('A string');

print(type(secondVariable));
print((secondVariable));

print(type(thirdVariable));
print((thirdVariable));

print(type(fourthVariable));
print((fourthVariable));

print(type(fifthVariable));
print((fifthVariable));