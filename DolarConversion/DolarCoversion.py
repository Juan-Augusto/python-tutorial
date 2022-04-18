from forex_python.converter import CurrencyRates

current_value = CurrencyRates().convert('USD', 'BRL', 1)
wallet = float(input('How much money do you have in your wallet in BRL? '))
print("The current value of the dollar in BRL is: {}".format(current_value))
print("You have {} USD in your wallet".format(wallet / current_value))