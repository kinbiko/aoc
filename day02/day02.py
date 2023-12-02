# Input format for reference:
# Game 6: 1 green, 3 blue; 2 blue, 9 red; 2 green, 13 blue, 11 red; 7 red, 12 blue, 1 green

def part1(input):
    legal = {'red': 12, 'green': 13, 'blue': 14}
    sum = 0
    for line in input.splitlines():
        game, draws = line.split(':')
        game_id = int(game.split()[1])
        for draw in draws.split('; '):
            pairs = [pair.split() for pair in draw.split(', ')]
            if not all([int(count) <= legal[color] for count, color in pairs]):
                break
        else:
            sum += game_id
    return sum


def part2(input):
    sum = 0
    for line in input.splitlines():
        draws = line.split(':')[1]
        # avoid multiplication with 0 if a color is missing from all draws in a game
        max_col = {'red': 1, 'green': 1, 'blue': 1}
        for draw in draws.split('; '):
            pairs = [pair.split() for pair in draw.split(', ')]
            for count, color in pairs:
                max_col[color] = max(max_col[color], int(count))
        sum += max_col['red'] * max_col['green'] * max_col['blue']
    return sum


with open('example.txt', 'r') as f:
    ex = f.read().rstrip("\n")
with open('input.txt', 'r') as f:
    input = f.read().rstrip("\n")

tests = {
    "part 1, example": {"want": 8, "got": part1(ex)},
    "part 1, input": {"want": 2176, "got": part1(input)},
    "part 2, example": {"want": 2286, "got": part2(ex)},
    "part 2, input": {"want": 63700, "got": part2(input)},
}

for name, test in tests.items():
    want = test['want']
    got = test['got']
    if want != got:
        print(f'{name}: wanted {want}, got {got}')
        break
else:
    print("ok")
