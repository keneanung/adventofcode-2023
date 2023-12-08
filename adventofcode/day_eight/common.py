from dataclasses import dataclass
from itertools import cycle
from math import lcm
import re
from typing import Iterable, Callable


NODE_REGEX = re.compile(r"^(\w{3}) = \((\w{3}), (\w{3})\)")

@dataclass
class Node():
    left: str
    right: str
    name: str

class Map():
    def __init__(self):
        self.__directions: str = ""
        self.__nodes: dict[str, Node] = {}
        
    def set_directions(self, directions: str):
        self.__directions = directions
        
    def add_node(self, name: str, left: str, right: str):
        self.__nodes[name] = Node(name=name, left=left, right=right)
        
    def get_steps(self, node_name: str, end_condition: Callable[[str], bool]):
        steps = 0
        for direction in cycle(self.__directions):
            if direction != "L" and direction != "R":
                    continue
            steps += 1
            node = self.__nodes[node_name]
            if direction == "R":
                node_name = node.right
            else:
                node_name  = node.left
            if end_condition(node_name):
                return steps
        raise Exception("Not reachable")
    
    def get_steps_one(self):
        return self.get_steps("AAA", lambda name: name=="ZZZ")
    
    def get_steps_two(self):
        lengths = [self.get_steps(node_name, lambda node_name: node_name.endswith("Z")) for node_name in self.__nodes.keys() if node_name.endswith("A")]
        return lcm(*lengths)

def parse_input(inp: Iterable[str]) -> Map:
    result = Map()
    for (index, line) in enumerate(inp):
        if index == 0:
            result.set_directions(line)
        node_match = re.match(NODE_REGEX, line)
        if node_match is not None:
            result.add_node(name=node_match.group(1), left=node_match.group(2), right=node_match.group(3))
            
    return result