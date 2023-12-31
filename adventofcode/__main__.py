from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.document import Document
from prompt_toolkit.validation import Validator, ValidationError

from adventofcode.day_one import puzzle_one as day_one_puzzle_one, puzzle_two as day_one_puzzle_two
from adventofcode.day_two import puzzle_one as day_two_puzzle_one, puzzle_two as day_two_puzzle_two
from adventofcode.day_three import puzzle_one as day_three_puzzle_one, puzzle_two as day_three_puzzle_two
from adventofcode.day_four import puzzle_one as day_four_puzzle_one, puzzle_two as day_four_puzzle_two
from adventofcode.day_five import puzzle_one as day_five_puzzle_one, puzzle_two as day_five_puzzle_two
from adventofcode.day_seven import puzzle_one as day_seven_puzzle_one, puzzle_two as day_seven_puzzle_two
from adventofcode.day_eight import puzzle_one as day_eight_puzzle_one, puzzle_two as day_eight_puzzle_two


PUZZLES = {
    "1": {
        "1": day_one_puzzle_one.run_puzzle,
        "2": day_one_puzzle_two.run_puzzle
    },
    "2":{
        "1": day_two_puzzle_one.run_puzzle,
        "2": day_two_puzzle_two.run_puzzle,
    },
    "3":{
        "1": day_three_puzzle_one.run_puzzle,
        "2": day_three_puzzle_two.run_puzzle,
    },
    "4":{
        "1": day_four_puzzle_one.run_puzzle,
        "2": day_four_puzzle_two.run_puzzle,
    },
    "5":{
        "1": day_five_puzzle_one.run_puzzle,
        "2": day_five_puzzle_two.run_puzzle,
    },
    "7":{
        "1": day_seven_puzzle_one.run_puzzle,
        "2": day_seven_puzzle_two.run_puzzle,
    },
    "8":{
        "1": day_eight_puzzle_one.run_puzzle,
        "2": day_eight_puzzle_two.run_puzzle,
    },
}

class DayValidator(Validator):
    def validate(self, document: Document) -> None:
        text = document.text
        if text and text not in PUZZLES.keys():
            raise ValidationError(message="There is no solved puzzle for that day yet.")

class PuzzleValidator(Validator):
    def __init__(self, day: str):
        self._day = day
        
    def validate(self, document: Document) -> None:
        text = document.text
        if text and text not in PUZZLES[self._day].keys():
            raise ValidationError(message="This puzzle has not been solved yet.")

answer_day = prompt("Which days puzzle would you like to get the answer for: ", completer=WordCompleter(list(PUZZLES.keys())), complete_while_typing=True, validator=DayValidator(), validate_while_typing=False)
answer_puzzle = prompt("Which puzzle would you like to solve: ", completer=WordCompleter(list(PUZZLES[answer_day].keys())), complete_while_typing=True, validator=PuzzleValidator(answer_day), validate_while_typing=False)
PUZZLES[answer_day][answer_puzzle]()