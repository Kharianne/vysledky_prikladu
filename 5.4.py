# Napiš program, do kterého může uživatel zadat dvě čísla.
# Program vypíše podíl čísel. Pokud by však podíl byl větší než 1000,
# tak vypiš jejich součet.

input1 = int(input("Number one: "))
input2 = int(input("Number two: "))

if input1/input2 > 1000:
    print(input1 + input2)
else:
    print(input1/input2)
