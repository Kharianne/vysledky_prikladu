# Napiš program, který vypíše pomocí cyklů následující:
# 1 + 1 = 2
# 1 + 2 = 3
# .
# .
# 1 + 9 = 10
# .
# 10 + 1 = 11
# .
# .
# .
# .
# 10 + 9 = 19

for i in range(1, 11):
    for j in range(1, 10):
        print("{} + {} = {}".format(i, j, i+j))
