from day_22 import PLAYER_1_DECK, PLAYER_2_DECK, play_game_of_combat


if __name__ == "__main__":
    winner = play_game_of_combat(PLAYER_1_DECK, PLAYER_2_DECK)
    print(winner.game_score)
