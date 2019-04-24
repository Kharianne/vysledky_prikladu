# Napiš program, který vezme od uživatele číslo
# a řekne mu, zdali je jeho číslo větší, menší nebo stejné,
# jako náhodně vygenerované číslo v programu.
import random

random_num = random.randint(0,500)

guessed_num = int(input("Give me number: "))

if random_num > guessed_num:
    print("Your number is lower than mine")
elif random_num < guessed_num:
    print("Your number is higher than mine")
else:
    print("Our numbers are the same")