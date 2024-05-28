import random

game_over = True
new_game = True
final_check = False
computer_hand = []
player_hand = []
scores = [0, 0]


def start_game():
    global computer_hand, player_hand, game_over
    game_over = False
    computer_hand = [random.randint(1, 12) for _ in range(2)]
    player_hand = [random.randint(1, 12) for _ in range(2)]
    check_hands(computer_hand, player_hand, final_check)


def draw_card():
    global computer_hand, player_hand, final_check
    draw = input("Draw another card? (Y/n): ")
    if draw.lower() in ["y", "ye", "yes"]:
        player_hand.append(random.randint(1, 12))
        if calculate_hand_value(computer_hand) <= 16:
            computer_hand.append(random.randint(1, 12))
    else:
        while calculate_hand_value(computer_hand) <= 16:
            computer_hand.append(random.randint(1, 12))
        final_check = True
    check_hands(computer_hand, player_hand, final_check)


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


def check_hands(computer_hand, player_hand, final_check):
    global scores, game_over
    computer_value = calculate_hand_value(computer_hand)
    player_value = calculate_hand_value(player_hand)

    display_computer_hand = computer_hand if final_check else computer_hand[:-1] + ['X']
    print(f"\nComputer's hand: {display_computer_hand}")
    print(f"Player's hand: {player_hand}")

    # Handle all final checks or immediate win-loss conditions
    if final_check or player_value >= 21 or computer_value >= 21:
        if computer_value == 21 and player_value == 21:
            print("\nPush! Nobody wins.")
        elif computer_value > 21 and player_value > 21:
            print("\nBoth players bust! It's a draw.")
        elif computer_value == 21 or (player_value < computer_value <= 21):
            print("\nBlackjack or higher value! Computer wins.")
            scores[0] += 1
        elif player_value == 21 or (computer_value < player_value <= 21):
            print("\nBlackjack or higher value! You won.")
            scores[1] += 1
        elif computer_value > 21:
            print("\nComputer busts! You won.")
            scores[1] += 1
        elif player_value > 21:
            print("\nYou bust! Computer wins.")
            scores[0] += 1
        else:
            # Compare scores if no one busts or blackjacks
            if player_value > computer_value:
                print("\nYou have a higher hand! You won.")
                scores[1] += 1
            else:
                print("\nComputer has a higher hand or it's a tie! Computer wins.")
                scores[0] += 1
        game_over = True


def show_scores(scores):
    global new_game
    print(f"Computer score: {scores[0]}\nPlayer score: {scores[1]}")
    keep_playing = input("Rematch? (Y/n): ")
    if keep_playing.lower() in ["y", "ye", "yes"]:
        return 0
    else:
        new_game = False


while new_game:
    start_game()
    while not game_over:
        draw_card()
    show_scores(scores)
