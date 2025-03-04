import random

# Function to get the computer's choice
def computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

# Function to determine the winner
def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'scissors' and computer == 'paper') or \
         (user == 'paper' and computer == 'rock'):
        return "You win!"
    else:
        return "You lose!"

# Main game loop
def play_game():
    print("Welcome to Rock, Paper, Scissors!")
    user_score = 0
    computer_score = 0

    while True:
        # Ask the user to choose rock, paper, or scissors
        user_choice = input("\nEnter your choice (rock, paper, or scissors): ").lower()

        # Check if the user input is valid
        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice! Please enter 'rock', 'paper', or 'scissors'.")
            continue

        # Get the computer's choice
        comp_choice = computer_choice()
        print(f"Computer chose: {comp_choice}")

        # Determine the winner
        result = determine_winner(user_choice, comp_choice)
        print(result)

        # Update the score
        if result == "You win!":
            user_score += 1
        elif result == "You lose!":
            computer_score += 1

        # Display the current scores
        print(f"Scores - You: {user_score}, Computer: {computer_score}")

        # Ask the user if they want to play again
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("\nThanks for playing! Final scores:")
            print(f"You: {user_score}, Computer: {computer_score}")
            break

# Run the game
play_game()
