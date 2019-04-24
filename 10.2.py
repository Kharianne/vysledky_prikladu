# Napiš program, který se bude neustále uživatele ptát na číslo,
# dokud uživatel nezadá opravdu číslo.

is_not_number = True
while is_not_number:
    try:
        number = int(input("Give me a number: "))
        is_not_number = False
    except ValueError:
        continue
