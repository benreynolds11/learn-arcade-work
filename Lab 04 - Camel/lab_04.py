import random


def game_over():
    end = input("Would you like to play again? (Yes/No) ")
    if end.upper() == "Yes":
        main()
    if end.upper() == "No":
        print("You are dead.")


def main():
    print("Welcome to Camel!")
    print("You have stolen a camel to make your way across the great Mobi desert.")
    print("The natives want their camel back and are chasing you down! Survive your")
    print("desert trek and out run the natives.")

    done = False

    # Variables
    camel_health = 0
    thirst = 0
    miles_traveled = 0
    natives_traveled = -20
    canteen = 3
    oasis = -1

    while not done:
        print()
        print("A. Drink from canteen")
        print("B. Ahead moderate speed.")
        print("C. Ahead full speed")
        print("D. Stop for the night.")
        print("E. Status check")
        print("Q. Quit")
        print()

        # Take user's input
        user_input = input("What will you do?")

        # If player quits
        if user_input.upper() == "Q":
            done = True
            print("You Quit")

        # Status check
        elif user_input.upper() == "E":
            print("Miles traveled:", miles_traveled)
            print("Drinks in canteen:", canteen)
            print("The natives are", miles_traveled - natives_traveled, "miles behind you.")
            print()

        # Stop for the night
        elif user_input.upper() == "D":
            print("You stop for the night.")
            print("Your camel is happy.")
            print("The natives don't stop.")
            print()

        # Full speed ahead
        elif user_input.upper() == "C":
            miles = random.randrange(12, 18)
            miles_traveled += miles
            thirst += 20
            camel_health += random.randrange(10,15)
            natives_traveled += random.randrange(7, 15)
            oasis = random.randrange(20)
            if oasis == 10:
                thirst = 0
                camel_health = 0
                canteen = 3
                print("As you travel you find an oasis!")
                print("You fill your canteen with water, and")
                print("Your camel regains full health!")
                print("The natives are still chasing you.")
                print()
            else:
                print("You continue moving a total of", miles, "miles.")
                print("Your getting more thirsty!")
                print("The natives are still chasing you.")
                print()

        # Mid speed ahead
        elif user_input.upper() == "B":
            miles = random.randrange(5, 12)
            miles_traveled += miles
            thirst += 10
            camel_health += 5
            natives_traveled += random.randrange(2, 9)
            oasis = random.randrange(20)
            if oasis == 10:
                thirst = 0
                camel_health = 0
                canteen = 3
                print("As you travel you find an oasis!")
                print("You fill your canteen with water, and")
                print("Your camel regains full health!")
                print("The natives are still chasing you.")
                print()
            else:
                print("You continue moving a total of", miles, "miles.")
                print("Your getting thirsty!")
                print("The natives are still chasing.")
                print()

        # Drink from canteen
        elif user_input.upper() == "A":
            if canteen > 0 :
                canteen -= 1
                thirst = 0
                print("You take a drink")
            else:
                print("Your canteen is empty.")

        # Thirst
        if thirst > 100:
            print("You died of thirst")
            print("Game Over.")
            print()
            done = True
        elif thirst > 50:
            print("You are thirsty!")

        # Distance traveled
        if miles_traveled >= 25:
            print("Congratulations! You have reached safety!")
            print("You win!")
            print()
            done = True
        # Camels health
        if camel_health > 35:
            print("Your camel died of exhaustion!")
            print("The natives caught up to you and kill you!")
            print("Game over.")
            print()
            done = True
        elif camel_health > 20:
            print("Your camel is tired.")
            print()

        # Natives distance
        if miles_traveled - natives_traveled <= 0:
            print("The natives have caught up to you!")
            print("They kill both you and your camel")
            print("Game Over.")
            print()
            done = True
        elif miles_traveled - natives_traveled < 15:
            print("Go faster! The natives are catching up!")
            print()



main()