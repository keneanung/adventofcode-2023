from typing import Iterable
from adventofcode.day_seven.common import run_specific_puzzle, solve_puzzle as solve_puzzle_common

def solve_puzzle(inp: Iterable[str]):
    return solve_puzzle_common(inp, True)

def run_puzzle():
    run_specific_puzzle(True)