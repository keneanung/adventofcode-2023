from adventofcode.day_eight.puzzle_one import solve_puzzle


def test_solution_case_1():
    inp = [
        "RL",
        "",
        "AAA = (BBB, CCC)",
        "BBB = (DDD, EEE)",
        "CCC = (ZZZ, GGG)",
        "DDD = (DDD, DDD)",
        "EEE = (EEE, EEE)",
        "GGG = (GGG, GGG)",
        "ZZZ = (ZZZ, ZZZ)",
    ]
    
    output = solve_puzzle(inp)
    
    assert output == 2


def test_solution_case_2():
    inp = [
        "LLR",
        "",
        "AAA = (BBB, BBB)",
        "BBB = (AAA, ZZZ)",
        "ZZZ = (ZZZ, ZZZ)",
    ]
    
    output = solve_puzzle(inp)
    
    assert output == 6