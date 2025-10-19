''' We all have played snake, water gun game in our childhood. If you haven’t, google the 
rules of this game and write a python program capable of playing this game with the 
user. '''

# Snake-Water-Gun game (CLI) --- snake > water, water > gun, gun > snake

import random

CHOICES = ("snake", "water", "gun")

def get_computer_choice():
    """Return computer's random choice."""
    return random.choice(CHOICES)

def get_user_choice():
    """
    Ask user for their choice.
    Accepts full words or first letters: s, w, g.
    Returns the normalized choice or None if user wants to quit.
    """
    while True:
        raw = input("Enter your choice (snake/s or water/w or gun/g) or 'q' to quit: ").strip().lower()
        if raw == 'q':
            return None
        if raw in ("snake", "s"):
            return "snake"
        if raw in ("water", "w"):
            return "water"
        if raw in ("gun", "g"):
            return "gun"
        print("Invalid input. Try again.")

def decide_winner(user, comp):
    """
    Decide winner:
      returns "user" if user wins,
              "comp" if computer wins,
              "tie" if tie.
    Rules:
      snake > water
      water > gun
      gun > snake
    """
    if user == comp:
        return "tie"

    wins = {
        ("snake", "water"),
        ("water", "gun"),
        ("gun", "snake"),
    }
    if (user, comp) in wins:
        return "user"
    else:
        return "comp"

def play_round():
    user = get_user_choice()
    if user is None:
        return None  # user chose to quit
    comp = get_computer_choice()
    print(f"You chose: {user}    Computer chose: {comp}")
    result = decide_winner(user, comp)
    if result == "tie":
        print("It's a tie!\n")
    elif result == "user":
        print("You win this round! 🎉\n")
    else:
        print("Computer wins this round. 😅\n")
    return result

def play_game():
    print("Welcome to Snake-Water-Gun!")
    print("Rules: snake > water, water > gun, gun > snake\n")

    # Choose number of rounds (optional)
    while True:
        rounds_input = input("Enter number of rounds to play (or press Enter for infinite until 'q'): ").strip()
        if rounds_input == "":
            total_rounds = None
            break
        try:
            total_rounds = int(rounds_input)
            if total_rounds <= 0:
                print("Enter a positive integer or leave blank.")
            else:
                break
        except ValueError:
            print("Please enter a valid integer or leave blank.")

    user_score = comp_score = ties = 0
    played = 0

    while True:
        # stop if fixed number of rounds reached
        if total_rounds is not None and played >= total_rounds:
            break

        result = play_round()
        if result is None:  # user quit
            print("You chose to quit the game.")
            break

        played += 1
        if result == "user":
            user_score += 1
        elif result == "comp":
            comp_score += 1
        else:
            ties += 1

        # show running score
        print(f"Score -> You: {user_score}  Computer: {comp_score}  Ties: {ties}  (Rounds played: {played})")
        print("-" * 50)

    # final summary
    print("\nFinal results:")
    print(f"Rounds played: {played}")
    print(f"You: {user_score}  Computer: {comp_score}  Ties: {ties}")
    if user_score > comp_score:
        print("Congrats — you won the game! 🏆")
    elif comp_score > user_score:
        print("Computer won the game. Better luck next time!")
    else:
        print("The game is a draw!")

if __name__ == "__main__":
    play_game()



