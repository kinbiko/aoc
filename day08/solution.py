from math import gcd

class Walker:
    def __init__(self, network, lr: str, here: str) -> None:
        self.network = network
        self.lr = lr
        self.here = here
        self.steps = 0

    def step(self):
        self.steps += 1
        self.here = self.network[self.here][0 if self.lr[0] == "L" else 1]
        self.lr = self.lr[1:] + self.lr[0]

def part1(input):
    lr, _, *node_map = input.splitlines()
    network = {line[:3]: (line[7:10], line[12:15]) for line in node_map}

    w = Walker(network, lr, "AAA")
    while w.here != "ZZZ":
        w.step()
    return w.steps

def part2(input):
    lr, _, *node_map = input.splitlines()
    network = {line[:3]: (line[7:10], line[12:15]) for line in node_map}

    start_positions = [node for node in network if node.endswith("A")]
    walkers = [Walker(network, lr, start) for start in start_positions]
    lcm = 1
    for walker in walkers:
        while not walker.here.endswith("Z"):
            walker.step()
        lcm *= walker.steps // gcd(lcm, walker.steps)
    return lcm

with open('example.txt', 'r') as f:
    ex = f.read().rstrip("\n")
with open('example_2.txt', 'r') as f:
    ex_2 = f.read().rstrip("\n")
with open('input.txt', 'r') as f:
    input = f.read().rstrip("\n")

tests = {
    "part 1, example": {"want": 2, "in": ex, "fn": part1},
    "part 1, input": {"want": 14429, "in": input, "fn": part1},
    "part 2, example": {"want": 6, "in": ex_2, "fn": part2},
    "part 2, input": {"want": 10921547990923, "in": input, "fn": part2},
}

for name, test in tests.items():
    want = test['want']
    got = test["fn"](test["in"])
    if want != got:
        print(f'{name}: wanted {want}, got {got}')
        break
else:
    print("ok")
