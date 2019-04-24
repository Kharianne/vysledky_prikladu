# Napiš program, který přečte vstup od uživatele
# - stranu a, b - a vypočítá obsah a obvod obdélníku.
# Výpočet realizuj funkcí.


def rectangle(a, b):
    obvod = 2 * (a + b)
    obsah = a * b
    return obvod, obsah


input1 = int(input("Zadejte stranu a: "))
input2 = int(input("Zadejte stranu b: "))

print(rectangle(input1, input2))
