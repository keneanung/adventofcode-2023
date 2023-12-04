from pathlib import Path
from typing import Iterable

from adventofcode.day_four.common import parse_input
from adventofcode.util import read_input


def solve_puzzle(inp: Iterable[str]) -> int:
    cards = parse_input(inp)
    winning_numbers_per_card = [len(card.winning_numbers.intersection(card.numbers_on_card)) for card in cards]
    __generate_copies(cards, winning_numbers_per_card)
    card_copies = [card.copies for card in cards]
    return sum(card_copies)

def __generate_copies(cards, winning_numbers_per_card):
    for (index, card) in enumerate(cards):
        winning_number = winning_numbers_per_card[index]
        if winning_number == 0:
            continue
        for additional_copy_index in range(index + 1, index + 1 + winning_number):
            if additional_copy_index >= len(cards):
                break
            cards[additional_copy_index].copies += card.copies

def run_puzzle():
    lines = read_input(Path(__file__).parent / "input.txt")
    print(solve_puzzle(lines))