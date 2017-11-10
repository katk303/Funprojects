def main():
    # setup: lunch options sorted by distance (walkable or no) and cuisine
    walk_asian = ["Arirang", "Golden Wok", "Ambar India", "Spoon House", "Midsummer Lounge", "Tang Dynasty",
                  "Lao Sze Chuan"]
    drive_asian = ["Kofusion", "Basil Thai", "Golden Harbor", "Szechuan China"]
    walk_american = ["Bread Company", "Daily Byte", "Burger King", "Beckman Cafe", "Cracked"]
    drive_american = ["Black Dog", "Farrens", "Merry Ann's", "Crane Alley", "Pekara"]
    walk_other = ["Manolo's", "Dragonfire", "Red Herring", "Timpone's", "Juanito's"]
    drive_other = ["Maize", "Huaraches Moroleones", "Rosati's", "Pizza M", "Manzanella's"]
    # selector for preferred cuisine
    mood = input("Are you in the mood for Asian, American, or Other? ")
    # selector for distance
    car = input("Do you want to walk or drive? ")
    # import for randomizing
    import random
    # function for randomizing
    def lunch_today(mood, car):
        # if walking:
        if car.lower() == "walk":
            if mood.lower() == "asian":
                return random.choice(walk_asian)
            elif mood.lower() == "american":
                return random.choice(walk_american)
            else:
                return random.choice(walk_other)
                # if driving:
        if car.lower() == "drive":
            if mood.lower() == "asian":
                return random.choice(drive_asian)
            elif mood.lower() == "american":
                return random.choice(drive_american)
            else:
                return random.choice(drive_other)

    # call/print lunch_today function
    print(lunch_today(mood, car))
    # allow for a mulligan
    eh = input("Do you want another option? y/n ")
    #allow for the vicissitudes of hunger and group input
    change_mood = input("Still in the mood for " + mood + "? y/n")
    # function for re-run -- needs to eliminate first choice****
    def not_that_place(eh, lunch_today):
        if eh.lower() == "y":
            if change_mood.lower() == "y":
                return lunch_today(mood, car)
            else:
                new_mood = input("Asian, American, or Other? ")
                return lunch_today(new_mood,car)
        else:
            return "Cool. Enjoy your lunch!"

    # call/print second try
    print(not_that_place(eh, lunch_today))


if __name__ == "__main__":
    main()
