import random
print(" Rock-Paper-Scissors Game! ")
while True:
    play_game = input("Wanna play Rock, Paper, Scissors? (yes/no): ").lower()
    if play_game == "no":
        print("Thankz for playing!")
        break
    elif play_game != "yes":
        print("Invalid input.enter 'yes' or 'no'.")
        continue
        # Get the user's choice
    user_choice = input("Choose rock or paper, or scissors: ").lower()
    while user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please choose rock or paper or scissors.")
        user_choice = input("Choose rock or paper or scissors: ").lower()
        # Get the computer's choice
    computer_choice = random.choice(["rock", "paper", "scissors"])
        # Determine the winner
    if user_choice == computer_choice:
        output = "It is a tie!"
    elif (
        (user_choice == "rock" and computer_choice == "scissors")
        or (user_choice == "paper" and computer_choice == "rock")
        or (user_choice == "scissors" and computer_choice == "paper")):
        output = "You win!"
    else:
        output = "You lose!"
    # Display the results of the game
    print(f"You choice is {user_choice}, the computer choice is {computer_choice}.")
    print(output)