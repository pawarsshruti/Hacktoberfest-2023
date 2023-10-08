import random

def game():
    choices = ["snake", "water", "gun"]

    player_score = 0
    computer_score = 0
    rounds = 0

    while rounds < 10:  # You can adjust the number of rounds
        computer_choice = random.choice(choices)

        player_choice = input("Enter your choice (snake/water/gun): ").lower()

        if player_choice not in choices:
            print("Invalid input! Please enter snake, water, or gun.")
            continue

        print(f"Computer chose: {computer_choice}")
        print(f"You chose: {player_choice}")

        if player_choice == computer_choice:
            print("It's a tie!")
        elif player_choice == "snake":
            if computer_choice == "water":
                print("You win! Snake drinks water.")
                player_score += 1
            else:
                print("Computer wins! Gun shoots snake.")
                computer_score += 1
        elif player_choice == "water":
            if computer_choice == "gun":
                print("You win! Water douses the gun.")
                player_score += 1
            else:
                print("Computer wins! Snake drinks water.")
                computer_score += 1
        elif player_choice == "gun":
            if computer_choice == "snake":
                print("You win! Gun shoots snake.")
                player_score += 1
            else:
                print("Computer wins! Water douses the gun.")
                computer_score += 1

        rounds += 1

    if player_score > computer_score:
        print("Congratulations! You win the game.")
    elif player_score < computer_score:
        print("Computer wins the game. Better luck next time!")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    print("Welcome to the Snake-Water-Gun game!")
    game()
