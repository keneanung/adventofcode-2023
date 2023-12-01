from curses.ascii import isdigit
from pathlib import Path
from typing import Iterable

from ..util import read_input

NUMBERS = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

NUMBER_STARTERS = [key[0] for key in NUMBERS.keys()]

def search_spelled_out_number(string_to_search: str) -> str | None:
    if string_to_search[0] in NUMBER_STARTERS:
        for number_word in NUMBERS.keys():
            if string_to_search.startswith(number_word):
                return NUMBERS[number_word]

def check_for_number(index: int, character: str, string_to_search: str):
    if character.isdigit():
        return character
    else:
        number = search_spelled_out_number(string_to_search[index:])
        if number is not None:
            return number
    return None

def find_first_number(string_to_search: str) -> str:
    for (index, character) in enumerate(string_to_search):
        number = check_for_number(index, character, string_to_search)
        if number is not None:
            return number
        
    raise Exception("No number found")
        
def find_last_number(string_to_search: str) -> str:
    for index in reversed(range(len(string_to_search))):
        number = check_for_number(index, string_to_search[index], string_to_search)
        if number is not None:
            return number
        
    raise Exception("No number found")

def solve_puzzle(inp: Iterable[str]) -> int:
    return sum([int(find_first_number(line) + find_last_number(line)) for line in inp])

def run_puzzle():
    lines = read_input(Path(__file__).parent / "input.txt")
    print(solve_puzzle(lines))