class Game:
    def __init__(self, line):
        self.winning, self.have = line.split(':')[1].split('|')
        self.count = 1

    def winners(self):
        w, h = self.winning.split(), self.have.split()
        return len(set(w).intersection(h))

    def score(self):
        return int(2**(self.winners()-1))

def part1(input):
    return sum([Game(line).score() for line in input.splitlines()])

def part2(input):
    games = [Game(line) for line in input.splitlines()]
    for i, game in enumerate(games):
        for j in range(game.winners()):
            games[i+j+1].count += game.count
    return sum([game.count for game in games])

with open('example.txt', 'r') as f:
    ex = f.read().rstrip("\n")
with open('input.txt', 'r') as f:
    input = f.read().rstrip("\n")

tests = {
    "part 1, example": {"want": 13, "got": part1(ex)},
    "part 1, input": {"want": 21959, "got": part1(input)},
    "part 2, example": {"want": 30, "got": part2(ex)},
    "part 2, input": {"want": 5132675, "got": part2(input)},
}

for name, test in tests.items():
    want = test['want']
    got = test['got']
    if want != got:
        print(f'{name}: wanted {want}, got {got}')
        break
else:
    print("ok")
