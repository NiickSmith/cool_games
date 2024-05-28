import random


# Function to start a new game
def start_game():
    computer_hand = [random.randint(1, 12) for _ in range(2)]
    player_hand = [random.randint(1, 12) for _ in range(2)]
    final_check = False  # Ensure final_check is reset at the start of each game
    return computer_hand, player_hand, final_check


# Function to handle drawing a card
def draw_card(computer_hand, player_hand, final_check):
    draw = input("Draw another card? (Y/n): ").strip().lower() if not final_check else ""
    if draw in ["y", "ye", "ys", "yes", "yep", "ya", "yas", "yea", "yeah", "yuh", "yup", "si"]:
        player_hand.append(random.randint(1, 12))
    else:
        final_check = True

    while calculate_hand_value(computer_hand) <= 16:
        computer_hand.append(random.randint(1, 12))

    return computer_hand, player_hand, final_check


# Function to calculate the value of a hand
def calculate_hand_value(hand):
    value = 0
    num_aces = hand.count(1)
    for card in hand:
        if card > 10:
            value += 10
        elif card == 1:
            value += 11
        else:
            value += card
    while value > 21 and num_aces:
        value -= 10
        num_aces -= 1
    return value


# Function to check the hands of both players
def check_hands(computer_hand, player_hand, final_check):
    computer_value = calculate_hand_value(computer_hand)
    player_value = calculate_hand_value(player_hand)

    display_computer_hand = computer_hand if final_check else computer_hand[:-1] + ['X']
    print(f"\nComputer's hand: {display_computer_hand}")
    print(f"Player's hand: {player_hand}")

    game_over = False
    result = None
    if final_check or (player_value >= 21 or computer_value >= 21):
        result = determine_winner(computer_value, player_value)
        game_over = True

    return game_over, result


# Function to determine the winner
def determine_winner(computer_value, player_value):
    if computer_value > 21 and player_value > 21:
        return "Both players bust! It's a draw."
    elif computer_value == 21 and player_value == 21:
        return "Push! Nobody wins."
    elif computer_value == 21:
        return "Blackjack! Computer wins."
    elif player_value == 21:
        return "Blackjack! You won."
    elif computer_value > 21:
        return "Computer busts! You won."
    elif player_value > 21:
        return "You bust! Computer wins."
    elif computer_value == player_value:
        return "It's a push! Nobody wins."
    else:
        if player_value > computer_value:
            return "You have a higher hand! You won."
        elif computer_value > player_value:
            return "Computer has a higher hand! Computer wins."
        else:
            return "Push! Nobody wins."


# Function to display scores
def show_scores(scores):
    print(f"Computer score: {scores[0]}\nPlayer score: {scores[1]}")
    keep_playing = input("Rematch? (Y/n): ").strip().lower()
    return keep_playing in ["y", "ye", "ys", "yes", "yep", "ya", "yas", "yea", "yeah", "yuh", "yup", "si"]


# Main function to run the game
def main():
    scores = [0, 0]
    new_game = True

    while new_game:
        computer_hand, player_hand, final_check = start_game()
        game_over, result = check_hands(computer_hand, player_hand, final_check)
        if not game_over:
            while not game_over:
                computer_hand, player_hand, final_check = draw_card(computer_hand, player_hand, final_check)
                game_over, result = check_hands(computer_hand, player_hand, final_check)
        print(f"\n{result}\nFinal: Computer hand: {computer_hand}\n\t   Player hand: {player_hand}")
        if "You won" in result:
            scores[1] += 1
        elif "Computer wins" in result:
            scores[0] += 1
        new_game = show_scores(scores)
    print("\nThanks for playing! Have a great day.")


if __name__ == "__main__":
    main()
