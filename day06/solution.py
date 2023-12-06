import math

def possible_wins(t, d):
    # See memo.md
    # https://www.youtube.com/watch?v=IvXgFLV2gOk
    left = 1/2 * (t - math.sqrt(t**2 - 4 * d)) + 1 # + 1 to account for exact integers
    right = 1/2 * (t + math.sqrt(t**2 - 4 * d))
    return math.ceil(right) - math.floor(left)

def part1(input):
    times = input.splitlines()[0].split()[1:]
    distances = input.splitlines()[1].split()[1:]
    product = 1
    for i in range(len(times)):
        product *= possible_wins(int(times[i]), int(distances[i]))
    return product

def part2(input):
    return part1(input)

with open('example_1.txt', 'r') as f:
    ex_1 = f.read().rstrip("\n")
with open('example_2.txt', 'r') as f:
    ex_2 = f.read().rstrip("\n")
with open('input_1.txt', 'r') as f:
    input_1 = f.read().rstrip("\n")
with open('input_2.txt', 'r') as f:
    input_2 = f.read().rstrip("\n")

tests = {
    "part 1, example": {"want": 288, "got": part1(ex_1)},
    "part 1, input": {"want": 1155175, "got": part1(input_1)},
    "part 2, example": {"want": 71503, "got": part2(ex_2)},
    "part 2, input": {"want": 35961505, "got": part2(input_2)},
}

for name, test in tests.items():
    want = test['want']
    got = test['got']
    if want != got:
        print(f'{name}: wanted {want}, got {got}')
        break
else:
    print("ok")
