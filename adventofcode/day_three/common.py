# The tuples here are coordinates. And since I'm dumb and switched the coordinates
# in the test and too lazy to turn them around, the tuples have the order of (y,x)
from dataclasses import dataclass
import re
from typing import Iterable, TypedDict


ADJACENT_COORDINATE_DIFFERENCES: Iterable[tuple[int, int]] = ((-1, 0), (0, -1), (1, 0), (0, 1), (-1,-1), (1,-1), (-1,1), (1,1))
__SYMBOL_REGEX = re.compile(r"[^\d.\s]")
__NUMBER_REGEX = re.compile(r"(\d+)")

@dataclass(frozen=True, eq=True)
class Symbol():
  x_coord: int
  y_coord: int
  symbol: str

@dataclass(frozen=True, eq=True)
class Number():
  """
  Class representing a number in the schematic. The x and y coordinates are used as an ID to be able to use them in sets.
  """
  x_coord: int
  y_coord: int
  value: int

@dataclass(eq=True)
class Schematic():
  symbols: set[Symbol]
  numbers: dict[tuple[int,int], Number]

def parse_input(inp: Iterable[str]) -> Schematic:
  result = Schematic(symbols=set(), numbers={})
  for (index, line) in enumerate(inp):
    for match in re.finditer(__SYMBOL_REGEX, line):
      result.symbols.add(Symbol(y_coord=index, x_coord=match.start(), symbol=match.group(0)))
    for match in re.finditer(__NUMBER_REGEX, line):
      for x_coord in range(match.start(), match.end()):
        result.numbers[(index, x_coord)] = Number(value=int(match.group(1)),y_coord=index, x_coord=match.start())

  return result