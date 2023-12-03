def mining_game():
    print("=== Welcome to the Galactic Mining Adventure ===")
    print("You find yourself aboard the cutting-edge mining spaceship, 'Star Digger,' in the heart of a vast asteroid belt.")
    print("Your mission: Navigate the cosmos, make strategic choices, and strike it rich with valuable resources!\n")

    # Start of the game
    print("=== Launch Sequence Initiated ===")
    first_choice = input("Do you initiate the launch sequence? (yes/no): ").lower()
    if first_choice == "yes":
        print("\nLaunching the Star Digger into the unknown!")
        second_choice = input("Two asteroids emerge on your radar. Mine the shimmering asteroid or the dense metallic one? (shimmer/metal): ").lower()

        if second_choice == "shimmer":
            print("\nVenturing towards the shimmering asteroid.")
            print("Your mining lasers uncover a rare crystal, gleaming with untold value!")
            print("=== Congratulations! You've struck cosmic fortune! ===")

        elif second_choice == "metal":
            print("\nHeading for the dense metallic asteroid.")
            third_choice = input("Continue mining or return to the ship for analysis? (mine/return): ").lower()

            if third_choice == "mine":
                print("\nDelving deeper into the metallic asteroid, you strike a rich deposit of precious metals!")
                print("=== Hooray! A successful mining haul! ===")

            else:
                print("\nReturning to the ship for safety. As you leave, the asteroid shifts, causing some equipment damage.")
                print("=== Game Over! Setbacks in your mining expedition. ===")

        else:
            print("\nInvalid choice! Wasting time on an uninteresting asteroid.")
            print("=== Game Over! Inefficient mining expedition. ===")

    elif first_choice == "no":
        print("\nDecision made not to launch. Reviewing mining data from the ship.")
        print("=== The adventure ends here. Avoided potential risks. ===")

    else:
        print("\nInvalid choice! Technical issues encountered before launch.")
        print("=== Game Over! Mining expedition canceled. ===")

    print("\n=== Thank you for playing the Galactic Mining Adventure! ===")

# Start the mining game
mining_game()
