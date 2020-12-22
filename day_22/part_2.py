from typing import Tuple

from day_22 import PLAYER_1_DECK, PLAYER_2_DECK, Deck


def play_round_of_recursive_combat(deck_1: Deck, deck_2: Deck):
    deck_1_card = deck_1.draw_card()
    deck_2_card = deck_2.draw_card()
    if len(deck_1.cards) >= deck_1_card and len(deck_2.cards) >= deck_2_card:
        new_deck_1, new_deck_2 = deck_1.copy(deck_1_card), deck_2.copy(deck_2_card)
        _, deck_1_is_winner = play_game_of_recursive_combat(new_deck_1, new_deck_2)
    else:
        deck_1_is_winner = deck_1_card > deck_2_card

    winning_deck = deck_1 if deck_1_is_winner else deck_2
    winning_deck.add_cards([deck_1_card, deck_2_card] if deck_1_is_winner else [deck_2_card, deck_1_card])


def play_game_of_recursive_combat(deck_1: Deck, deck_2: Deck) -> Tuple[Deck, bool]:
    previous_configurations = set()
    while deck_1.cards and deck_2.cards:
        previous_configurations.add((tuple(deck_1.cards), tuple(deck_2.cards)))
        play_round_of_recursive_combat(deck_1, deck_2)
        if (tuple(deck_1.cards), tuple(deck_2.cards)) in previous_configurations:
            return deck_1, True

    return (deck_1 if deck_1.cards else deck_2), bool(deck_1.cards)


if __name__ == "__main__":
    winner, _ = play_game_of_recursive_combat(PLAYER_1_DECK, PLAYER_2_DECK)
    print(winner.game_score)
