from pathlib import Path
import re
from typing import Iterable

from adventofcode.day_four.common import parse_input
from adventofcode.util import read_input


def solve_puzzle(inp: Iterable[str]) -> int:
    cards = parse_input(inp)
    winning_numbers_on_cards = [card.winning_numbers.intersection(card.numbers_on_card) for card in cards]
    points_per_card = [2**(len(winning_numbers)-1) for winning_numbers in winning_numbers_on_cards if len(winning_numbers) > 0]
    return sum(points_per_card)

def run_puzzle():
    lines = read_input(Path(__file__).parent / "input.txt")
    print(solve_puzzle(lines))