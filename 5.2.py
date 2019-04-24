# Napiš program, který od uživatele přečte den v týdnu
# a řekne mu, zdali je to všední den nebo den víkendu.

day = input("Give me a name of day: ")

if day.lower() in ["saturday", "sunday"]:
    print("It is a weekend day")
elif day.lower() in ["monday", "tuesday", "wednesday", "thursday", "friday"]:
    print("It is a weekday")
else:
    print("It is not a valid day in week in English.")
