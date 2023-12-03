from pathlib import Path
from typing import Iterable
from adventofcode.day_three.common import Number, Schematic, parse_input

from adventofcode.util import read_input


def find_adjacent_numbers(schematic: Schematic) -> Iterable[Number]:
  adjacent_numbers = set()
  number_coordinates = schematic.numbers.keys()
  for symbol in schematic.symbols:
    for (dy, dx) in ((-1, 0), (0, -1), (1, 0), (0, 1), (-1,-1), (1,-1), (-1,1), (1,1)):
      adjacent_coordinates = (symbol.y_coord + dy, symbol.x_coord + dx)
      if adjacent_coordinates in number_coordinates:
        adjacent_numbers.add(schematic.numbers[(adjacent_coordinates)])

  return adjacent_numbers

def solve_puzzle(inp: Iterable[str]) -> int:
  schematic = parse_input(inp)
  adjacent_numbers = find_adjacent_numbers(schematic)
  numbers_only = [number.value for number in adjacent_numbers]
  return sum(numbers_only)

def run_puzzle():
    lines = read_input(Path(__file__).parent / "input.txt")
    print(solve_puzzle(lines))