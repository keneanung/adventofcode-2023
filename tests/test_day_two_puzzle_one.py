from adventofcode.day_two.puzzle_one import parse_input, solve_puzzle


def test_parser():
    inp= [
        "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
        "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
        "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
        "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
        "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
    ] 
    
    output = parse_input(inp)
    
    assert output == {
        1: [{"blue": 3, "red": 4}, {"blue": 6, "red": 1, "green": 2}, {"green": 2}],
        2: [{"blue": 1, "green": 2}, {"blue": 4, "red": 1, "green": 3}, {"blue": 1, "green": 1}],
        3: [{"blue": 6, "red": 20, "green": 8}, {"blue": 5, "red": 4, "green": 13}, {"red": 1, "green": 5}],
        4: [{"blue": 6, "red": 3, "green": 1}, {"red": 6, "green": 3}, {"blue": 15, "red": 14, "green": 3}],
        5: [{"blue": 1, "red": 6, "green": 3}, {"blue": 2, "red": 1, "green": 2}],
    }

def test_solution():
    inp= [
        "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
        "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
        "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
        "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
        "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
    ]

    output = solve_puzzle(inp)

    assert output == 8