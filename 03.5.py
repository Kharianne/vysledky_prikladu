# Problémy s opicemi. Máme dvě opice.
# Když se opice úsmívá považujme to, jako True v pythonu, když se opice neusmívá
# označme to jako False.
# Když se obě opice usmívají nebo se nesměje ani jedna jsme v potížích.
# Napiš takovou funkci, která bude brát dva parametry a (True, False)
# a vypíše, jestli jsme v potížích nebo ne.


def am_i_in_trouble(monkey1, monkey2):
    if (monkey1 and monkey2) or (not monkey1 and not monkey2):
        return "You are in trouble"
    else:
        return "You are not in trouble"

# Testy
print(am_i_in_trouble(True, True))
print(am_i_in_trouble(False, True))
print(am_i_in_trouble(True, False))
print(am_i_in_trouble(False, False))


