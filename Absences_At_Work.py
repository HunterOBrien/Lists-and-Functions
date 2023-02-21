nameDict = {}

zeroAbsence = []


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
            most_days_ab = max(nameDict.values())
            print(f"The average number of days of absences is "
                  f"{abs_days_ave:.2f} days")

            for i in nameDict:
                if nameDict[i] == most_days_ab:
                    print("The person with the most days absent is: ")
                    print(i)

            for nonAbsent in nameDict:
                if nameDict[nonAbsent] == 0:
                    zeroAbsence.append(nonAbsent)

            for aboveAve in nameDict:
                if nameDict[aboveAve] > abs_days_ave:
                    print(f"{aboveAve} was absent for more than the average of {abs_days_ave:.2f} with {nameDict[aboveAve]} days absent")
            print(", ".join(zeroAbsence), "were both absent for zero days")
            null = 0


absences()
