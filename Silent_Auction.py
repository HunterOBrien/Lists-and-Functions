def silent_auction():
    item = input("What is the Auction Item: ")
    reserve = float(input("What is the Reserve of the Item: "))
    highest_bid = 0
    current_bid = 0
    while current_bid != -1:
        current_bid = float(input("What is your bid: "))
        if current_bid > highest_bid:
            highest_bid = current_bid
            print(f"The current highest bid is ${highest_bid}")

        else:
            print("Please enter a higher bid")

    if highest_bid >= reserve:
        print(
            f"Congratulations, the auction ended with a highest bid of ${highest_bid}")

    else:
        print(f"The Highest Bid of ${highest_bid} did not meet the reserve")


silent_auction()
