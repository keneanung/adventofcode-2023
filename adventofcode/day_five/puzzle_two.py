from dataclasses import dataclass
from pathlib import Path
import re
from typing import Iterable, TypedDict

from adventofcode.util import read_input

SEED_LINE_REGEX = re.compile(r"^seeds: (.+)$")
SEED_REGEX = re.compile(r"(\d+) (\d+)")
MAP_REGEX = re.compile(r"^[^-]+-to-(\w+) map:$")
MAP_LINE_REGEX = re.compile(r"^(\d+) (\d+) (\d+)$")

@dataclass()
class MapInfo():
    source_start: int
    destination_start: int
    map_range: int

class SeedIterator():
    ranges: list[tuple[int,int]]
    __current_range: int
    __current_value: int
    
    def __init__(self):
        self.__current_range = 0
        self.__current_value = 0
        self.ranges = []
        
    def add_range(self, start: int, length: int):
        self.ranges.append((start, length))
    
    def __iter__(self):
        self.__current_range = 0
        self.__current_value = self.ranges[self.__current_range][0] - 1
        return self
    
    def __next__(self):
        current_range = self.ranges[self.__current_range]
        next_candidate = self.__current_value + 1
        if next_candidate < current_range[0] + current_range[1]:
            self.__current_value = next_candidate
            return self.__current_value
        next_range_candidate = self.__current_range + 1
        if next_range_candidate < len(self.ranges):
            print(next_range_candidate)
            self.__current_range = next_range_candidate
            self.__current_value = self.ranges[self.__current_range][0]
            return self.__current_value
        raise StopIteration

class Almanac():
    
    def __init__(self):
        self.seeds: SeedIterator = SeedIterator()
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
                result.seeds.add_range(start=int(seed_match.group(1)), length=int(seed_match.group(2)))
            continue
        match = re.match(MAP_REGEX, line)
        if match is not None:
            current_map = match.group(1)
            continue
        match = re.match(MAP_LINE_REGEX, line)
        if match is not None:
            result[current_map].append(MapInfo(destination_start=int(match.group(1)), source_start=int(match.group(2)), map_range=int(match.group(3))))
    return result

def get_minimum_seed_location(almanac: Almanac)->int:
    current_min = 1000000000000000000000000000000000000000000000000
    seeds = set()
    for seed in almanac.seeds:
        if seed in seeds:
            continue
        seeds.add(seed)
        step = seed
        for map in ("soil", "fertilizer", "water", "light", "temperature", "humidity", "location"):
            step = get_mapped_thing(almanac, map, step)
        current_min = min(current_min, step)
    return current_min
        
def get_mapped_thing(almanac: Almanac, map: str, step:int) -> int:
    map_info_list = almanac[map]
    for map_info in map_info_list:
        diff = step - map_info.source_start
        if diff >= 0 and diff < map_info.map_range:
            return map_info.destination_start + diff
    return step

def solve_puzzle(inp: Iterable[str]) -> int:
    almanac = parse_input(inp)
    locations = get_minimum_seed_location(almanac)
    return locations

def run_puzzle():
    lines = read_input(Path(__file__).parent / "input.txt")
    print(solve_puzzle(lines))