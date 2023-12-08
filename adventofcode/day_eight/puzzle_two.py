from pathlib import Path
from typing import Iterable
from adventofcode.day_eight.common import parse_input

from adventofcode.util import read_input


def solve_puzzle(inp: Iterable[str]) -> int:
    map = parse_input(inp)
    return map.get_steps_two()

def run_puzzle():
    lines = read_input(Path(__file__).parent / "input.txt")
    print(solve_puzzle(lines))