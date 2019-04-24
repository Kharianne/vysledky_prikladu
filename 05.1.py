# Napiš program, který od uživatele přečte číslo
# a řekne mu, zdali je sudé nebo liché.

number = int(input("Give me a number: "))
if number % 2 == 0:
    print("Your number is even.")
else:
    print("Your number is odd.")