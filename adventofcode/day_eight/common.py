from dataclasses import dataclass
from itertools import cycle
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
        
    def get_steps(self, path_nodes: Iterable[str], end_condition: Callable[[list[str]], bool]):
        steps = 0
        for direction in cycle(self.__directions):
            if direction != "L" and direction != "R":
                    continue
            steps += 1
            new_path_nodes: list[str] = []
            for node_name in path_nodes:
                node = self.__nodes[node_name]
                if direction == "R":
                    node_name = node.right
                else:
                    node_name  = node.left
                new_path_nodes.append(node_name)
            path_nodes = new_path_nodes
            if steps % 1000000 == 0:
                print(steps)
            if end_condition(new_path_nodes):
                return steps
        raise Exception("Not reachable")
    
    def get_steps_one(self):
        return self.get_steps(["AAA"], lambda lst: lst[0]=="ZZZ")
    
    def get_steps_two(self):
        starts = [node_name for node_name in self.__nodes.keys() if node_name.endswith("A")]
        print(len(starts))
        end_condition = lambda nodes: not any(not node_name.endswith("Z") for node_name in nodes)
        return self.get_steps(starts, end_condition)

def parse_input(inp: Iterable[str]) -> Map:
    result = Map()
    for (index, line) in enumerate(inp):
        if index == 0:
            result.set_directions(line)
        node_match = re.match(NODE_REGEX, line)
        if node_match is not None:
            result.add_node(name=node_match.group(1), left=node_match.group(2), right=node_match.group(3))
            
    return result