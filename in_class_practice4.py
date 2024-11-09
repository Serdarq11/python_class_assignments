#Import the random module
import random


# Get user input and validate it
while True:
    while True:
        try:
            user_input = int(input("Enter your dice roll (a number between 1 and 6): "))
            if 1 <= user_input <= 6:
                break
            else:
                print("Please enter a valid number between 1 and 6.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 6.")


    # Simulate computer's roll
    computer_roll = random.randint(1, 6)
    
    
    # Determine the winner
    print(f"\nYou rolled: {user_input}")
    print(f"Computer rolled: {computer_roll}")

    if user_input > computer_roll:
        print("You win!")
    elif user_input < computer_roll:
        print("Computer wins!")
    else:
        print("It's a tie!")


    # Ask if the user wants to play again
    play_again = input("\nDo you want to play again? Enter 'q' to quit or any other key to continue: ")
    if play_again.lower() == 'q':
        print("Thanks for playing!")
        break

