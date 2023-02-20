nameDict = {
    "Michael": 80,
    "Ethan": 23,
    "Hunter": 12,
    "Bob": 0,
    "Jimmy": 0,
}


def absences():
    null = 1
    while null == 1:
        absence = input("Do you want to record a Absence? (yes or $ "
                        "for no) ").lower()
        while absence not in ("yes", "$"):
            absence = input("Do you want to record a Absence? (yes or $ "
                            "for no) ").lower()
        if absence == "yes":
            name = input("What is the name of the employee? ").capitalize()
            days_off = int(input(f"How many days has {name} been absent? "))
            nameDict[name] = days_off
        else:
            abs_days_ave = sum(nameDict.values()) / len(nameDict.values())
            name_most_days_abs = max(nameDict.values())

            abs_days_none = [zero_days_abs[0] for zero_days_abs in nameDict]
            print(abs_days_none)

            print(f"The average number of days of absences is "
                  f"{abs_days_ave:.2f} days")
            # Gets the key for the person with the most days absent from the value and prints
            print("The person with the most days absent is: ",
                  list(nameDict.keys())
                  [list(nameDict.values()).index(name_most_days_abs)])

            null = 0


absences()
