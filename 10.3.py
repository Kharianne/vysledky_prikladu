# Napiš program, který od uživatele vezme 3 čísla
# a pak vrátí to největší z nich.
# Nepoužívej funkci max().

number1 = int(input("Number: "))
number2 = int(input("Number: "))
number3 = int(input("Number: "))

if number1 > number2 and number1 > number3:
    print(number1)
elif number2 > number1 and number2 > number3:
    print(number2)
else:
    print(number3)
