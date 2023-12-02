from pathlib import Path
from typing import Iterable

from adventofcode.day_two.common import GameReveal, parse_input, reduce_to_max
from adventofcode.util import read_input

def __is_possible(game: list[GameReveal]) -> bool:
  max_reveal = reduce_to_max(game)
  return (max_reveal["red"] <= 12) and (max_reveal["green"] <= 13) and (max_reveal["blue"] <= 14) 


def solve_puzzle(input: Iterable[str]) -> int:
  games = parse_input(input)
  return sum([game for game in games if __is_possible(games[game])])

def run_puzzle():
    lines = read_input(Path(__file__).parent / "input.txt")
    print(solve_puzzle(lines))