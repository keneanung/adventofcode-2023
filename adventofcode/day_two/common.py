import re
from typing import Iterable, TypedDict


class GameReveal(TypedDict):
  blue: int
  red: int
  green: int

__GAME_REGEX = re.compile(r"^Game (\d+): (.+)$")
__COLOUR_REGEX = re.compile(r"^(\d+) (\w+)$")

def parse_input(input: Iterable[str])->dict[int,list[GameReveal]]:
  result = {}
  for line in input:
    __parse_line(result, line)
  return result

def __parse_line(result, line):
    game_matches = re.match(__GAME_REGEX, line)
    id = int(game_matches.group(1))
    result[id] = []
    reveals = game_matches.group(2).split(";")
    for reveal in reveals:
      colours_revealed = __parse_reveal(reveal)  
      result[id].append(colours_revealed)

def __parse_reveal(reveal):
    colours_revealed = GameReveal()
    colours = reveal.split(",")
    for colour in colours:
      __parse_colour(colours_revealed, colour)
    return colours_revealed

def __parse_colour(colours_revealed, colour):
    colour = colour.strip()
    colour_matches = re.match(__COLOUR_REGEX, colour)
    colours_revealed[colour_matches.group(2)] = int(colour_matches.group(1))

def reduce_to_max(game: list[GameReveal]) -> GameReveal:
  result = GameReveal()
  result["red"] = 0
  result["green"] = 0
  result["blue"] = 0
  for reveal in game:
    for colour in reveal:
      result[colour] = max(result[colour], reveal[colour])
  return result