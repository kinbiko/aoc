from math import gcd
from collections import namedtuple
from dataclasses import dataclass

@dataclass
class Walker:
    network: dict[str, tuple[str, str]]
    lr: str
    here: str
    steps = 0

    def step(self):
        self.steps += 1
        self.here = self.network[self.here][0 if self.lr[0] == "L" else 1]
        self.lr = self.lr[1:] + self.lr[0]

def part1(input):
    lr, _, *node_map = input.splitlines()
    network = {line[:3]: (line[7:10], line[12:15]) for line in node_map}

    walker = Walker(network=network, lr=lr, here="AAA")
    while walker.here != "ZZZ":
        walker.step()
    return walker.steps

def part2(input):
    lr, _, *node_map = input.splitlines()
    network = {line[:3]: (line[7:10], line[12:15]) for line in node_map}

    start_positions = [node for node in network if node.endswith("A")]
    walkers = [Walker(network=network, lr=lr, here=start) for start in start_positions]
    lcm = 1
    for walker in walkers:
        while not walker.here.endswith("Z"):
            walker.step()
        lcm *= walker.steps // gcd(lcm, walker.steps)
    return lcm

Test = namedtuple("Test", ["name", "fn", "file", "want"])
tests = [
    Test(fn=part1, name="part 1, example", file="example.txt",   want=2),
    Test(fn=part1, name="part 1, input",   file="input.txt",     want=14429),
    Test(fn=part2, name="part 2, example", file="example_2.txt", want=6),
    Test(fn=part2, name="part 2, input",   file="input.txt",     want=10921547990923),
]

for (name, fn, file, want) in tests:
    with open(file, 'r') as f:
        input = f.read().rstrip("\n")
    got = fn(input)
    if want != got:
        print(f'{name}: wanted {want}, got {got}')
        break
else:
    print("ok")
