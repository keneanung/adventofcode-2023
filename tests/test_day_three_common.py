from adventofcode.day_three.common import Number, Schematic, Symbol, parse_input


def test_parser():
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

  output = parse_input(inp)

  assert output == Schematic(
    symbols={
      Symbol(y_coord=1,x_coord=3,symbol="*"),
      Symbol(y_coord=3,x_coord=6,symbol="#"),
      Symbol(y_coord=4,x_coord=3,symbol="*"),
      Symbol(y_coord=5,x_coord=5,symbol="+"),
      Symbol(y_coord=8,x_coord=3,symbol="$"),
      Symbol(y_coord=8,x_coord=5,symbol="*")
    },
    numbers={
      (0,0): Number(value=467, y_coord=0, x_coord=0),
      (0,1): Number(value=467, y_coord=0, x_coord=0),
      (0,2): Number(value=467, y_coord=0, x_coord=0),
      (0,5): Number(value=114, y_coord=0, x_coord=5),
      (0,6): Number(value=114, y_coord=0, x_coord=5),
      (0,7): Number(value=114, y_coord=0, x_coord=5),
      (2,2): Number(value=35, y_coord=2, x_coord=2),
      (2,3): Number(value=35, y_coord=2, x_coord=2),
      (2,6): Number(value=633, y_coord=2, x_coord=6),
      (2,7): Number(value=633, y_coord=2, x_coord=6),
      (2,8): Number(value=633, y_coord=2, x_coord=6),
      (4,0): Number(value=617, y_coord=4, x_coord=0),
      (4,1): Number(value=617, y_coord=4, x_coord=0),
      (4,2): Number(value=617, y_coord=4, x_coord=0),
      (5,7): Number(value=58, y_coord=5, x_coord=7),
      (5,8): Number(value=58, y_coord=5, x_coord=7),
      (6,2): Number(value=592, y_coord=6, x_coord=2),
      (6,3): Number(value=592, y_coord=6, x_coord=2),
      (6,4): Number(value=592, y_coord=6, x_coord=2),
      (7,6): Number(value=755, y_coord=7, x_coord=6),
      (7,7): Number(value=755, y_coord=7, x_coord=6),
      (7,8): Number(value=755, y_coord=7, x_coord=6),
      (9,1): Number(value=664, y_coord=9, x_coord=1),
      (9,2): Number(value=664, y_coord=9, x_coord=1),
      (9,3): Number(value=664, y_coord=9, x_coord=1),
      (9,5): Number(value=598, y_coord=9, x_coord=5),
      (9,6): Number(value=598, y_coord=9, x_coord=5),
      (9,7): Number(value=598, y_coord=9, x_coord=5),
    }
  )