def trip_calculator():
    # Gets driver's name
    driver_name = input("What is your name: ").capitalize()

    # variables for later use
    cost_total = 0
    total_time = 0
    average_cost = 0
    average_time = 0
    trips = 0

    # ends the while loop
    null = 1

    # while the user wants to start a new trip the trip time is asked and variables are calculated
    while null == 1:
        do_you_want_to_start_a_new_trip = input(
            "Do you want to START A NEW TRIP: ").upper()
        if do_you_want_to_start_a_new_trip == "YES":
            trip_time = float(input("How long did the trip take (minutes): "))
            cost_total = cost_total + trip_time * 2 + 10
            total_time = total_time + trip_time
            trips = trips + 1

        # calculates the averages for cost and time then prints the details of the driver
        elif do_you_want_to_start_a_new_trip == "NO":
            average_cost = cost_total / trips
            average_time = total_time / trips
            print("\n")
            print(f"Driver: {driver_name}")
            print("==================================")
            print(f"Total Trip Time: {total_time:.2f}")
            print(f"Average Time for Trips: {average_time:.2f}")
            print(f"Total Income for Trips: ${cost_total:.2f}")
            print(f"Average Cost for Trips: {average_cost:.2f}")
            null = 0


trip_calculator()
