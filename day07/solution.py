from collections import namedtuple

Hand = namedtuple("Hand", ["cards", "bid"])

def score(cards):
    counts = [cards.count(card) for card in cards]

    if 5 in counts: return 6
    if 4 in counts: return 5
    if 3 in counts and 2 in counts: return 4
    if 3 in counts: return 3
    if counts.count(2) == 4: return 2
    if 2 in counts: return 1
    return 0

def solve(input: str, sorter):
    hands = []
    for line in input.splitlines():
        cards, bid = line.split()
        hands.append(Hand(cards, int(bid)))
    hands.sort(key=sorter)
    return sum(rank * hand.bid for rank, hand in enumerate(hands, 1))

# Part 1 specific:

basic_map = {
    "0": "0", "1": "1", "2": "2", "3": "3", "4": "4",
    "5": "5", "6": "6", "7": "7", "8": "8", "9": "9",
    # Give face cards ASCII values *above* 0123456789, in the correct order
    "T": "A", "J": "B", "Q": "C", "K": "D", "A": "E",
}

def basic_score(cards):
    return score(cards), *[basic_map.get(card) for card in cards]

# Part 2 specific:

joker_map = {
    "0": "0", "1": "1", "2": "2", "3": "3", "4": "4",
    "5": "5", "6": "6", "7": "7", "8": "8", "9": "9",
    # Give face cards ASCII values *above* 0123456789, in the correct order
    # J is now a Joker
    "T": "A", "J": "*", "Q": "C", "K": "D", "A": "E",
}

def combinations(cards):
    combos = [""]
    for card in cards:
        candidates = "23456789TQKA" if card == "J" else card
        combos = [prev + next for prev in combos for next in candidates]
    return combos


def joker_score(cards):
    return (
        max([score(r) for r in combinations(cards)]),
        [joker_map.get(card, card) for card in cards],
    )


def part1(input: str):
    return solve(input, lambda h: basic_score(h.cards))

def part2(input):
    return solve(input, lambda h: joker_score(h.cards))

with open('example.txt', 'r') as f:
    ex = f.read().rstrip("\n")
with open('input.txt', 'r') as f:
    input = f.read().rstrip("\n")

tests = {
    "part 1, example": {"want": 6440, "got": part1(ex)},
    "part 1, input": {"want": 249390788, "got": part1(input)},
    "part 2, example": {"want": 5905, "got": part2(ex)},
    "part 2, input": {"want": 248750248, "got": part2(input)},
}

for name, test in tests.items():
    want = test['want']
    got = test['got']
    if want != got:
        print(f'{name}: wanted {want}, got {got}')
        break
else:
    print("ok")
