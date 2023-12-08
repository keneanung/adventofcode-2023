from adventofcode.day_eight.puzzle_two import solve_puzzle


def test_solution_case():
    inp = [
        "LR",
        "",
        "11A = (11B, XXX)",
        "11B = (XXX, 11Z)",
        "11Z = (11B, XXX)",
        "22A = (22B, XXX)",
        "22B = (22C, 22C)",
        "22C = (22Z, 22Z)",
        "22Z = (22B, 22B)",
        "XXX = (XXX, XXX)",
    ]
    
    output = solve_puzzle(inp)
    
    assert output == 6