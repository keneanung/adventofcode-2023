from collections import Counter
from enum import Enum
from functools import total_ordering
from pathlib import Path
from typing import Iterable

from adventofcode.util import read_input

CARD_VALUE_JOKER = {
    "J": 0,
    "2": 1,
    "3": 2,
    "4": 3,
    "5": 4,
    "6": 5,
    "7": 6,
    "8": 7,
    "9": 8,
    "T": 9,
    "Q": 10,
    "K": 11,
    "A": 12
}

CARD_VALUE_NORMAL = {
    "2": 0,
    "3": 1,
    "4": 2,
    "5": 3,
    "6": 4,
    "7": 5,
    "8": 6,
    "9": 7,
    "T": 8,
    "J": 9,
    "Q": 10,
    "K": 11,
    "A": 12
}

class Kind(Enum):
    HIGH_CARD = 0
    PAIR = 1
    TWO_PAIRS = 2
    TRIPLE = 3
    FULL_HOUSE = 4
    QUARTET = 5
    QUINTUPLE = 6

@total_ordering
class Hand():
    def __init__(self, cards: str, bet: str, with_joker: bool):
        self.__cards = cards
        self.bet=int(bet)
        self.__with_joker=with_joker
        
    @property
    def kind(self) -> Kind:
        counts = Counter(self.__cards)
        if self.__with_joker:
            jokers = counts['J']
            del counts["J"]
        else:
            jokers = 0
        different_cards = len(counts)
        if different_cards == 1 or different_cards == 0:
            return Kind.QUINTUPLE
        sorted_count = sorted(counts.values(), reverse=True)
        if different_cards == 2:
            if sorted_count[0] + jokers == 4:
                return Kind.QUARTET
            if sorted_count[0] + jokers == 3:
                return Kind.FULL_HOUSE
        if different_cards == 3:
            if sorted_count[0] + jokers == 3:
                return Kind.TRIPLE
            if sorted_count[0] + jokers == 2:
                return Kind.TWO_PAIRS
        if different_cards == 4:
            return Kind.PAIR
        return Kind.HIGH_CARD
    
    def __eq__(self, other: "Hand"):
        return self.__cards == other.__cards
    
    def __lt__(self, other: "Hand"):
        if self.kind != other.kind:
            return self.kind.value < other.kind.value
        for index in range(len(self.__cards)):
            if self.__cards[index] != other.__cards[index]:
                values = CARD_VALUE_JOKER if self.__with_joker else CARD_VALUE_NORMAL
                return values[self.__cards[index]] < values[other.__cards[index]]
                
def __parse_input(inp: Iterable[str], with_joker: bool):
    result: list[Hand] = []
    for line in inp:
        parts = line.split(" ")
        result.append(Hand(parts[0], parts[1], with_joker))
    return result

def solve_puzzle(inp: Iterable[str], with_joker: bool) -> int:
    hands = __parse_input(inp, with_joker)
    sorted_hands = sorted(hands)
    return sum(hand.bet * (index+1) for (index, hand) in enumerate(sorted_hands))

def run_specific_puzzle(with_joker: bool):
    lines = read_input(Path(__file__).parent / "input.txt")
    print(solve_puzzle(lines, with_joker))