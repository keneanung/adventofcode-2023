from dataclasses import dataclass
from pathlib import Path
import re
from typing import Iterable, TypedDict

from adventofcode.util import read_input

SEED_LINE_REGEX = re.compile(r"^seeds: (.+)$")
SEED_REGEX = re.compile(r"\d+")
MAP_REGEX = re.compile(r"^[^-]+-to-(\w+) map:$")
MAP_LINE_REGEX = re.compile(r"^(\d+) (\d+) (\d+)$")

@dataclass()
class MapInfo():
    source_start: int
    destination_start: int
    map_range: int

class Almanac():
    
    def __init__(self):
        self.seeds: list[int] = []
        self.soil: list[MapInfo] = []
        self.fertilizer: list[MapInfo] = []
        self.water: list[MapInfo] = []
        self.light: list[MapInfo] = []
        self.temperature: list[MapInfo] = []
        self.humidity: list[MapInfo] = []
        self.location: list[MapInfo] = []
        
    def __getitem__(self, item):
        if item == "soil":
            return self.soil
        if item == "fertilizer":
            return self.fertilizer
        if item == "water":
            return self.water
        if item == "light":
            return self.light
        if item == "temperature":
            return self.temperature
        if item == "humidity":
            return self.humidity
        if item == "location":
            return self.location
        raise Exception(f"Unknown item '{item}'")
    
def parse_input(inp: Iterable[str]) -> Almanac:
    result = Almanac()
    current_map = "soil"
    for line in inp:
        match = re.match(SEED_LINE_REGEX, line)
        if match is not None:
            for seed_match in re.finditer(SEED_REGEX, match.group(1)):
                result.seeds.append(int(seed_match.group(0)))
            continue
        match = re.match(MAP_REGEX, line)
        if match is not None:
            current_map = match.group(1)
            continue
        match = re.match(MAP_LINE_REGEX, line)
        if match is not None:
            result[current_map].append(MapInfo(destination_start=int(match.group(1)), source_start=int(match.group(2)), map_range=int(match.group(3))))
    return result

def get_seed_locations(almanac: Almanac)->list[int]:
    result = []
    for seed in almanac.seeds:
        step = seed
        for map in ("soil", "fertilizer", "water", "light", "temperature", "humidity", "location"):
            step = get_mapped_thing(almanac, map, step)
        result.append(step)
    return result
        
def get_mapped_thing(almanac: Almanac, map: str, step:int) -> int:
    map_info_list = almanac[map]
    for map_info in map_info_list:
        diff = step - map_info.source_start
        if diff >= 0 and diff < map_info.map_range:
            return map_info.destination_start + diff
    return step

def solve_puzzle(inp: Iterable[str]) -> int:
    almanac = parse_input(inp)
    locations = get_seed_locations(almanac)
    return min(locations)

def run_puzzle():
    lines = read_input(Path(__file__).parent / "input.txt")
    print(solve_puzzle(lines))