from adventofcode.day_seven.puzzle_one import solve_puzzle


def test_solution():
    inp= [
        "32T3K 765",
        "T55J5 684",
        "KK677 28",
        "KTJJT 220",
        "QQQJA 483",
    ] 
    
    output = solve_puzzle(inp)
    
    assert output == 6440