from curses.ascii import isdigit
from pathlib import Path
from typing import Iterable

from ..util import read_input


def find_first_number(string_to_search: Iterable[str]) -> str:
    for character in string_to_search:
        if character.isdigit():
            return character
        
    raise Exception("No number found")
        
def find_last_number(string_to_search: str) -> str:
    return find_first_number(reversed(string_to_search))

def solve_puzzle(inp: Iterable[str]) -> int:
    return sum([int(find_first_number(line) + find_last_number(line)) for line in inp])

def run_puzzle():
    lines = read_input(Path(__file__).parent / "input.txt")
    print(solve_puzzle(lines))