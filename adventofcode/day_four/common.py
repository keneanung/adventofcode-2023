from dataclasses import dataclass
import re
from typing import Iterable


__CARD_REGEX = re.compile(r"^Card\s+\d+: ([\d\s]+) \| ([\d\s]+)$")

@dataclass
class Card():
    winning_numbers: set[int]
    numbers_on_card: set[int]
    copies: int

def __parse_card(line: str) -> Card:
    card_matches = re.match(__CARD_REGEX, line)
    result = Card(winning_numbers=set(), numbers_on_card=set(),copies=1)
    if card_matches is None:
        raise Exception(f'Did we get a card? Input: {line}')
    winning_string: str = card_matches.group(1)
    __parse_numbers(set_to_update=result.winning_numbers, number_string_to_parse=winning_string)
    
    numbers_on_card_string: str = card_matches.group(2)
    __parse_numbers(set_to_update=result.numbers_on_card, number_string_to_parse=numbers_on_card_string)
    return result

def __parse_numbers(set_to_update: set[int], number_string_to_parse: str):
    for number in number_string_to_parse.split(" "):
        number = number.strip()
        if number == "":
            continue
        set_to_update.add(int(number))

def parse_input(inp: Iterable[str]) -> list[Card]:
    result = []
    
    for line in inp:
        result.append(__parse_card(line))
    
    return result