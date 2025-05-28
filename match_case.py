day = input("Enter a day of the weel=k (Monday-Sunday): ").lower()

match day:
    case "monday":
        print("Ugh, it's Monday")
    case "tuesday":
        print("Just another work day")
    case "wednesday":
        print("Hump day!")
    case "thursday":
        print("Almost there")
    case "friday":
        print("It's Friday, let's go out!")
    case "saturday" | "sunday":
        print("It's the weekend, time to relax!")
    case _:
        print("That's not a valid day of the week")  # Default case if no match is found

        