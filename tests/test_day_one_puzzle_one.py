from adventofcode.day_one.puzzle_one import solve_puzzle


def test_solution():
    inp= [
        "1abc2",
        "pqr3stu8vwx",
        "a1b2c3d4e5f",
        "treb7uchet",
    ] 
    
    output = solve_puzzle(inp)
    
    assert output == 142