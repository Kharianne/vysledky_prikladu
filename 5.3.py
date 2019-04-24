# Napiš program, který vypíše pomocí cyklů následující:
# 1 1
# 1 2
# 1 3
# 1 4
# 2 1
# 2 2
# 2 3
# 2 4

for i in range(1, 3):
    for j in range(1, 5):
        print("{}  {}".format(i, j))
