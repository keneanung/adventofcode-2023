from adventofcode.day_one.puzzle_two import solve_puzzle


def test_solution():
    inp= [
        "two1nine",
        "eightwothree",
        "abcone2threexyz",
        "xtwone3four",
        "4nineeightseven2",
        "zoneight234",
        "7pqrstsixteen"
    ] 
    
    output = solve_puzzle(inp)
    
    assert output == 281