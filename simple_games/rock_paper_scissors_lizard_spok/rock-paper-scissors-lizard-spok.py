import random

# Dictionary to store the user's previous choices and the frequency of each choice
user_choices = {"rock": 0, "paper": 0, "scissors": 0, "lizard": 0, "spock": 0}

def get_user_choice():
    while True:
        user_choice = input("Enter your choice (rock, paper, scissors, lizard, Spock): ").lower()
        if user_choice in ["rock", "paper", "scissors", "lizard", "spock"]:
            return user_choice
        else:
            print("Invalid choice! Please enter rock, paper, scissors, lizard, or Spock.")

def get_computer_choice():
    # Strategy: Predict the user's next move based on their most frequent previous choice
    most_frequent_choice = max(user_choices, key=user_choices.get)
    
    # Generate a random choice, but with higher probability for the predicted choice
    choices = ["rock", "paper", "scissors", "lizard", "spock"]
    weighted_choices = [most_frequent_choice] * 3 + choices
    return random.choice(weighted_choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and (computer_choice == "scissors" or computer_choice == "lizard")) or \
         (user_choice == "paper" and (computer_choice == "rock" or computer_choice == "spock")) or \
         (user_choice == "scissors" and (computer_choice == "paper" or computer_choice == "lizard")) or \
         (user_choice == "lizard" and (computer_choice == "spock" or computer_choice == "paper")) or \
         (user_choice == "spock" and (computer_choice == "rock" or computer_choice == "scissors")):
        return "You win!"
    else:
        return "Computer wins!"

def update_user_choices(user_choice):
    user_choices[user_choice] += 1

def play_game():
    print("Let's play Rock-Paper-Scissors-Lizard-Spock!")
    rounds = int(input("Enter the number of rounds to play: "))
    user_score = 0
    computer_score = 0
    for round in range(1, rounds + 1):
        print(f"Round {round}:")
        user_choice = get_user_choice()
        update_user_choices(user_choice)
        computer_choice = get_computer_choice()
        print("You chose:", user_choice)
        print("Computer chose:", computer_choice)
        result = determine_winner(user_choice, computer_choice)
        print(result)
        if "You win" in result:
            user_score += 1
        elif "Computer wins" in result:
            computer_score += 1
        print(f"Score - You: {user_score}, Computer: {computer_score}")
    
    if user_score > computer_score:
        print("Congratulations! You win the game!")
    elif user_score < computer_score:
        print("Computer wins the game. Better luck next time!")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    play_game()
