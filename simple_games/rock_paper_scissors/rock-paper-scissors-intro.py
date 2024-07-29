# Introduction to Rock-Paper-Scissors Game 

# 1. User Input
user_choice = input("Enter your choice (high or low): ").lower() # .lower() will make all input lowercase

# 2. Conditional Statements
if user_choice == "high":
    print("You chose high!")
elif user_choice == "low":
    print("You chose low!")
else:
    print("Invalid choice! Please enter high or low.")

# 3. Random Selection
import random
computer_choice = random.choice(["high", "low"])
print("Computer chose:", computer_choice)

# 4. Determining the Winner
if user_choice == computer_choice:
    print("It's a tie!")
elif (user_choice == "high" and computer_choice == "low"):
    print("You win!")
else:
    print("Computer wins!")

# 5. Repeating the Game
while True:
    # enter code for playing game
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing!")
        break
