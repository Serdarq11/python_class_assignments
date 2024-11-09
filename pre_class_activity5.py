import random

# Simulate rolling a six-sided die and return its value
def roll_single_die():
    # Generate a random number between 1 and 6
    face_value = random.randrange(1, 7)
    return face_value

while True:
    double_count = 0
    rounds = input('How many rounds do you want to do? (Or ENTER to quit): ')
    
    if rounds == "":
        break
    
    try:
        rounds = int(rounds)
    except ValueError:
        print('Please enter an integer number.')
        continue  # Go back to the start of the while loop

    for current_round in range(rounds):
        die_one = roll_single_die()
        die_two = roll_single_die()
        
        if die_one == die_two:
            double_count += 1
    
    double_percentage = (double_count * 100.0) / rounds
    print('Out of', rounds, 'you rolled', double_count, 'doubles, or', double_percentage, '%')

print('OK Bye')
