# Napiš takovou funkci, která bude brát jako parametr slovo a číslo.
# Slovo pak bude v jednom stringu tolikrát, jaká je hodnota čísla např:
# funkce("baf", 3) vrátí bafbafbaf


def multiplier(word, a):
    return word * a


print(multiplier("baf", 3))
print(multiplier("po", 6))
