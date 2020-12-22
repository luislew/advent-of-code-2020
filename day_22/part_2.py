from typing import Tuple

from day_22 import PLAYER_1_DECK, PLAYER_2_DECK, Deck


def get_configuration(deck_1: Deck, deck_2: Deck) -> Tuple[Tuple[int, ...], Tuple[int, ...]]:
    return tuple(deck_1.cards), tuple(deck_2.cards)


def play_round_of_recursive_combat(deck_1: Deck, deck_2: Deck):
    deck_1_card, deck_2_card = deck_1.draw_card(), deck_2.draw_card()
    if deck_1_card > len(deck_1.cards) or deck_2_card > len(deck_2.cards):
        deck_1_is_winner = deck_1_card > deck_2_card
    else:
        new_deck_1, new_deck_2 = deck_1.copy(n=deck_1_card), deck_2.copy(n=deck_2_card)
        _, deck_1_is_winner = play_game_of_recursive_combat(new_deck_1, new_deck_2)

    if deck_1_is_winner:
        deck_1.add_cards(deck_1_card, deck_2_card)
    else:
        deck_2.add_cards(deck_2_card, deck_1_card)


def play_game_of_recursive_combat(deck_1: Deck, deck_2: Deck) -> Tuple[Deck, bool]:
    previous_configurations = set()
    while deck_1.cards and deck_2.cards:
        previous_configurations.add(get_configuration(deck_1, deck_2))
        play_round_of_recursive_combat(deck_1, deck_2)
        if get_configuration(deck_1, deck_2) in previous_configurations:
            return deck_1, True

    return deck_1 if deck_1.cards else deck_2, bool(deck_1.cards)


if __name__ == "__main__":
    winner, _ = play_game_of_recursive_combat(PLAYER_1_DECK, PLAYER_2_DECK)
    print(winner.game_score)
