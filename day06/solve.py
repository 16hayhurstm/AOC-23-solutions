from aocd import get_data, submit

YEAR = 2023


def part1(data):
    data = zip(*map(lambda x: map(int, x.split(":")[1].split()), data.split("\n")))
    combinations = 1
    for time, distance in data:
        num_ways_2beat = 0
        for i in range(time):
            if (i) * (time - i) > distance:
                num_ways_2beat += 1
        combinations *= num_ways_2beat
    print(combinations)
    return combinations


def part2(data):
    data = [map(lambda x: int("".join(x.split(":")[1].split())), data.split("\n"))]
    combinations = 1
    for time, distance in data:
        num_ways_2beat = 0
        for i in range(time):
            if (i) * (time - i) > distance:
                num_ways_2beat += 1
        combinations *= num_ways_2beat
    return combinations


def main():
    day = int(__file__.split("/")[-2][-2:])
    data = get_data(day=day, year=YEAR)
    p1 = part1(data)
    if p1:
        submit(p1, part="a", day=day, year=YEAR)
    p2 = part2(data)
    if p2:
        submit(p2, part="b", day=day, year=YEAR)


if __name__ == "__main__":
    main()
