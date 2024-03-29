from aocd import get_data, submit

YEAR = 2023


d = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""


def part1(data):
    l = data.split("\n")
    print(l)
    total_worth = 0
    for game in l:
        n = 0
        cards = game[9:].split("|")
        cards = list(map(str.split, cards))
        print((cards))
        for nums in cards[0]:
            if nums in cards[1]:
                n += 1
        if n > 0:
            a = 2 ** (n - 1)
            print(a)
            total_worth += a
    print(total_worth)
    return total_worth


def part2(data):
    l = data.split("\n")

    return None


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
