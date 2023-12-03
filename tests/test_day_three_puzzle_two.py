from adventofcode.day_three.puzzle_two import solve_puzzle

def test_solution():
  inp = [
    "467..114..",
    "...*......",
    "..35..633.",
    "......#...",
    "617*......",
    ".....+.58.",
    "..592.....",
    "......755.",
    "...$.*....",
    ".664.598..",
  ]

  output = solve_puzzle(inp)

  assert output == 467835