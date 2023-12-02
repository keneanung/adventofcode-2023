from pathlib import Path
from typing import Iterable

from adventofcode.day_two.common import parse_input, reduce_to_max
from adventofcode.util import read_input

def solve_puzzle(input: Iterable[str]) -> int:
  games = parse_input(input)
  minimum_cubes_per_game = [reduce_to_max(games[game]) for game in games]
  power_per_game = [game["blue"] * game["green"] * game["red"] for game in minimum_cubes_per_game]
  return sum(power_per_game)

def run_puzzle():
    lines = read_input(Path(__file__).parent / "input.txt")
    print(solve_puzzle(lines))