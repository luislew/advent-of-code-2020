import dataclasses
import os
import typing

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))


@dataclasses.dataclass
class Deck:
    cards: typing.List[int]

    @property
    def game_score(self) -> int:
        multipliers = range(len(self.cards), 0, -1)
        return sum(multiplier * card for multiplier, card in zip(multipliers, self.cards))

    def draw_card(self) -> int:
        return self.cards.pop(0)

    def add_cards(self, *cards: int):
        self.cards.extend(cards)

    def copy(self, n: int) -> "Deck":
        return Deck(self.cards.copy()[:n])


def get_data_from_input():
    with open(os.path.join(__location__, "input.txt")) as f:
        for line in f:
            yield line.strip()


def play_round_of_combat(deck_1: Deck, deck_2: Deck) -> None:
    deck_1_card, deck_2_card = deck_1.draw_card(), deck_2.draw_card()
    if deck_1_card > deck_2_card:
        deck_1.add_cards(deck_1_card, deck_2_card)
    else:
        deck_2.add_cards(deck_2_card, deck_1_card)


def play_game_of_combat(deck_1: Deck, deck_2: Deck) -> Deck:
    while deck_1.cards and deck_2.cards:
        play_round_of_combat(deck_1, deck_2)
    return deck_1 if deck_1.cards else deck_2


RAW_INPUT = list(get_data_from_input())
PLAYER_1_DECK = Deck([int(i) for i in RAW_INPUT[1:26]])
PLAYER_2_DECK = Deck([int(i) for i in RAW_INPUT[28:]])
