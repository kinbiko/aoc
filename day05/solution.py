class SoilMap:
    def __init__(self, block, next):
        self.ranges = []
        for line in block.splitlines()[1:]:
            self.ranges.append([int(v) for v in line.split()])
        self.next = next

    def find_locations_individual_seeds(self, seeds):
        next_input = []
        for seed in seeds:
            for drs, srs, rl in self.ranges:
                if srs <= seed < srs + rl:
                    next_input.append(seed - srs + drs)
                    break
            else:
                next_input.append(seed)

        if self.next != None:
            return self.next.find_locations_individual_seeds(next_input)
        return next_input

    def find_locations_intervals(self, seeds):
        next_input = []
        while len(seeds) > 0:
            start, end = seeds.pop()
            for drs, srs, rl in self.ranges:
                overlap_start = max(start, srs)
                overlap_end = min(end, srs + rl)
                if overlap_start < overlap_end:
                    delta = drs - srs
                    next_input.append((overlap_start + delta, overlap_end + delta))
                    if overlap_start > start:
                        seeds.append((start, overlap_start))
                    if end > overlap_end:
                        seeds.append((overlap_end, end))
                    break
            else:
                next_input.append((start, end))

        if self.next != None:
            return self.next.find_locations_intervals(next_input)
        return next_input

def part1(input):
    head, *tail = input.split("\n\n")

    humidity_to_location = SoilMap(tail[6], None)
    temperature_to_humidity = SoilMap(tail[5], humidity_to_location)
    light_to_temperature = SoilMap(tail[4], temperature_to_humidity)
    water_to_light = SoilMap(tail[3], light_to_temperature)
    fertilizer_to_water = SoilMap(tail[2], water_to_light)
    soil_to_fertilizer = SoilMap(tail[1], fertilizer_to_water)
    seed_to_soil = SoilMap(tail[0], soil_to_fertilizer)

    seeds = [int(s) for s in head.split(":")[1].split()]
    return min(seed_to_soil.find_locations_individual_seeds(seeds))

def part2(input):
    head, *tail = input.split("\n\n")

    humidity_to_location = SoilMap(tail[6], None)
    temperature_to_humidity = SoilMap(tail[5], humidity_to_location)
    light_to_temperature = SoilMap(tail[4], temperature_to_humidity)
    water_to_light = SoilMap(tail[3], light_to_temperature)
    fertilizer_to_water = SoilMap(tail[2], water_to_light)
    soil_to_fertilizer = SoilMap(tail[1], fertilizer_to_water)
    seed_to_soil = SoilMap(tail[0], soil_to_fertilizer)

    head = [int(s) for s in head.split(":")[1].split()]
    seed_intervals = []
    for i in range(0, len(head), 2):
        interval = (head[i], head[i] + head[i + 1])
        seed_intervals.append(interval)
    return min(seed_to_soil.find_locations_intervals(seed_intervals))[0]

with open('example.txt', 'r') as f:
    ex = f.read().rstrip("\n")
with open('input.txt', 'r') as f:
    input = f.read().rstrip("\n")

tests = {
    "part 1, example": {"want": 35, "got": part1(ex)},
    "part 1, input": {"want": 196167384, "got": part1(input)},
    "part 2, example": {"want": 46, "got": part2(ex)},
    "part 2, input": {"want": 125742456, "got": part2(input)},
}

for name, test in tests.items():
    want = test['want']
    got = test['got']
    if want != got:
        print(f'{name}: wanted {want}, got {got}')
        break
else:
    print("ok")
