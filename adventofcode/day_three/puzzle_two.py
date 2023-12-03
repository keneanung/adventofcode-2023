from pathlib import Path
from typing import Iterable, Sized
from adventofcode.day_three.common import ADJACENT_COORDINATE_DIFFERENCES, Number, Schematic, Symbol, parse_input

from adventofcode.util import read_input


GEAR_CANDIDATE = "*"

def find_gear_ratios(schematic: Schematic) -> Iterable[int]:
  gears_ratios = []
  all_number_coordinates = schematic.numbers.keys()
  for symbol in schematic.symbols:
    if symbol.symbol == GEAR_CANDIDATE:
      adjacent_numbers = find_adjacent_numbers(schematic, all_number_coordinates, symbol)
      if adjacent_numbers_qualify_symbol_as_gear(adjacent_numbers):
        adjacent_numbers_list = extract_number_values(adjacent_numbers)
        gears_ratios.append(calculate_gear_ratio(adjacent_numbers_list))

  return gears_ratios

def extract_number_values(adjacent_numbers: Iterable[Number]) -> tuple[int]:
    return tuple(adjacent_number.value for adjacent_number in adjacent_numbers)

def adjacent_numbers_qualify_symbol_as_gear(adjacent_numbers: Sized) -> bool:
    return len(adjacent_numbers) == 2

def find_adjacent_numbers(schematic: Schematic, all_number_coordinates: set[tuple[int, int]], symbol: Symbol) -> set[Number]:
    adjacent_numbers: set[Number] = set()
    for (dy, dx) in ADJACENT_COORDINATE_DIFFERENCES:
      adjacent_coordinates = (symbol.y_coord + dy, symbol.x_coord + dx)
      if adjacent_coordinates in all_number_coordinates:
        adjacent_numbers.add(schematic.numbers[adjacent_coordinates])
    return adjacent_numbers

def calculate_gear_ratio(adjacent_numbers_list: tuple[int]) -> int:
    return adjacent_numbers_list[0] * adjacent_numbers_list[1]

def solve_puzzle(inp: Iterable[str]) -> int:
  schematic = parse_input(inp)
  gear_ratios = find_gear_ratios(schematic)
  return sum(gear_ratios)

def run_puzzle():
    lines = read_input(Path(__file__).parent / "input.txt")
    print(solve_puzzle(lines))