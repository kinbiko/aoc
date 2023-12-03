import collections

DIRECTIONS = [
    [-1, -1], [0, -1],  [1, -1],
    [-1, 0],            [1, 0],
    [-1, 1],  [0, 1],   [1, 1],
]

def bounded(x, y, lines):
    in_bounds = lambda i,l: i>= 0 and i<l
    return in_bounds(x, len(lines)) and in_bounds(y, len(lines[0]))

def is_symbol(x, y, lines):
    is_symbol = lambda c: c !=  '.' and not c.isdigit()
    return bounded(x, y, lines) and is_symbol(lines[x][y])

def is_star(x, y, lines):
    return bounded(x, y, lines) and lines[x][y] == "*"


class Part1Engine:
    def __init__(self):
        self.total = 0
        self.symbol_adjacent = False
        self.current_number = ""
    
    def process(self, lines):
        for i, line in enumerate(lines):
            for j, c in enumerate(line):
                if not c.isdigit():
                    self.update()
                    continue

                self.current_number += c
                for (x, y) in DIRECTIONS:
                    self.symbol_adjacent |= is_symbol(i+x, j+y, lines)
            self.update()
        return self.total

    def update(self):
        if self.symbol_adjacent:
            self.total += int(self.current_number)
        self.symbol_adjacent = False
        self.current_number = ""


class Part2Enigne:
    def __init__(self) -> None:
        self.gears = collections.defaultdict(list)
        self.current_gear = None
        self.current_number = ''

    def process(self, lines):
        for i, line in enumerate(lines):
            for j, c in enumerate(line):
                if not c.isdigit():
                    self.update()
                    continue

                self.current_number += c
                for (x, y) in DIRECTIONS:
                    self.current_gear = (x+i, y+j) if is_star(x+i, y+j, lines) else self.current_gear
            self.update()

        return sum([gear[0] * gear[1] for gear in self.gears.values() if len(gear) == 2])

    def update(self):
        if self.current_gear:
            self.gears[self.current_gear].append(int(self.current_number))
        self.current_gear = None
        self.current_number = ''

def part1(input):
    return Part1Engine().process(input.splitlines())

def part2(input):
    return Part2Enigne().process(input.splitlines())

with open('example.txt', 'r') as f:
    ex = f.read().rstrip("\n")
with open('input.txt', 'r') as f:
    input = f.read().rstrip("\n")

tests = {
    "part 1, example": {"want": 4361, "got": part1(ex)},
    "part 1, input": {"want": 556367, "got": part1(input)},
    "part 2, example": {"want": 467835, "got": part2(ex)},
    "part 2, input": {"want": 89471771, "got": part2(input)},
}

for name, test in tests.items():
    want = test['want']
    got = test['got']
    if want != got:
        print(f'{name}: wanted {want}, got {got}')
        break
else:
    print("ok")
