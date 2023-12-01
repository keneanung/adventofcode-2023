from pathlib import Path
from typing import Iterable

from ..util import read_input

__NUMBERS = {
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

def __search_spelled_out_number(string_to_search: str) -> str | None:
    for number_word in __NUMBERS.keys():
        if string_to_search.startswith(number_word):
            return __NUMBERS[number_word]

def __check_for_number(index: int, character: str, string_to_search: str):
    if character.isdigit():
        return character
    else:
        number = __search_spelled_out_number(string_to_search[index:])
        if number is not None:
            return number
    return None

def __find_number(index_iterable: Iterable[int], string_to_search: str):
    for index in index_iterable:
        number = __check_for_number(index, string_to_search[index], string_to_search)
        if number is not None:
            return number
        
    raise Exception("No number found")

def __find_first_number(string_to_search: str) -> str:
    return __find_number(range(len(string_to_search)), string_to_search)
        
def __find_last_number(string_to_search: str) -> str:
    return __find_number(reversed(range(len(string_to_search))), string_to_search)

def solve_puzzle(inp: Iterable[str]) -> int:
    return sum([int(__find_first_number(line) + __find_last_number(line)) for line in inp])

def run_puzzle():
    lines = read_input(Path(__file__).parent / "input.txt")
    print(solve_puzzle(lines))