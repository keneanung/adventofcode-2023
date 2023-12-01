import fileinput
from pathlib import Path


def read_input(path_to_read: Path):
    return fileinput.input(path_to_read)
    