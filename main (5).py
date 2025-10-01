import random

CHOICES = ("rock", "paper", "scissors")

def get_computer_choice():
    return random.choice(CHOICES)

def get_user_choice():
    while True:
        choice = input("Enter rock, paper, or scissors (or 'q' to quit): ").strip().lower()
        if choice == 'q':
            return 'q'
        if choice in CHOICES:
            return choice
        print("Invalid choice. Please type rock, paper or scissors (or 'q' to quit).")

def decide_winner(user, computer):
    if user == computer:
        return "draw"
    # rock beats scissors, scissors beats paper, paper beats rock
    wins = {
        "rock": "scissors",
        "scissors": "paper",
        "paper": "rock"
    }
    return "user" if wins[user] == computer else "computer"

def main():
    print("Welcome to Rock, Paper, Scissors!")
    user_score = 0
    computer_score = 0
    rounds = 0

    while True:
        user = get_user_choice()
        if user == 'q':
            break
        computer = get_computer_choice()
        print(f"You chose: {user}    Computer chose: {computer}")

        winner = decide_winner(user, computer)
        if winner == "draw":
            print("It's a draw!")
        elif winner == "user":
            print("You win this round!")
            user_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1

        rounds += 1
        print(f"Score -> You: {user_score}  Computer: {computer_score}  Rounds played: {rounds}")
        print("-" * 40)

    print("\nThanks for playing!")
    print(f"Final Score -> You: {user_score}  Computer: {computer_score}  Rounds played: {rounds}")
    if user_score > computer_score:
        print("Overall winner: You 🎉")
    elif computer_score > user_score:
        print("Overall winner: Computer 🤖")
    else:
        print("Overall: Draw 🤝")

if __name__ == "__main__":
    main()