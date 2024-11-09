import random

def roll_dice():
    return random.randint(1, 6)

def play_round():
    user_score = 0
    computer_score = 0
    rounds = 5

    for i in range(rounds):
        user_roll = roll_dice()
        computer_roll = roll_dice()
        
        if user_roll > computer_roll:
            print(f"User wins! {user_roll} vs {computer_roll}")
            user_score += 1
        elif computer_roll > user_roll:
            print(f"Computer wins! {computer_roll} vs {user_roll}")
            computer_score += 1
        else:
            print(f"Draw no winner! {user_roll} vs {computer_roll}")

    print("\n--- Round Summary ---")
    print(f"User's total wins: {user_score}")
    print(f"Computer's total wins: {computer_score}")

    if user_score > computer_score:
        print("User wins the round!")
    elif computer_score > user_score:
        print("Computer wins the round!")
    else:
        print("The round is a draw!")

def main():
    print("Welcome to the Dice Rolling Game!")
    
    while True:
        user_input = input("Press 'y' to roll the dice, or any other key to quit: ").lower()
        
        if user_input == 'y':
            play_round()
        else:
            print("Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()
