nameDict = {

            }


def abs():
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
            abs_days_ave = sum(nameDict.values())/len(nameDict.values())
            name_most_days_abs = max(nameDict.values())
            print(f"The average number of days of absences is "
                  f"{abs_days_ave:.2f} days\n"
                  f"{name_most_days_abs} is the person with the most days "
                  f"absent\n")
            null = 0


abs()





