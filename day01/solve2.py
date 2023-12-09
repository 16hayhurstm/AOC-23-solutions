from aocd import get_data, submit
import re

YEAR = 2023


def part1(data):
    l = data.split("\n")
    new = []
    total = 0
    for item in l:
        new.append(("".join(i for i in item if i.isdigit())))
    for i in new:
        total += int(i[0] + i[-1])

    return total


dic_num2 = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

dic_num1 = {
    "oneight": 18,
    "twone": 21,
    "eighthree": 83,
    "eightwo": 82,
    "threeight": 38,
    "fiveight": 58,
    "sevenine": 79,
    "nineight": 98,
}


def replace_all(text):
    for i, j in dic_num1.items():
        text = text.replace(i, str(j))
    for i, j in dic_num2.items():
        text = text.replace(i, str(j))
    return text


def part2(data):
    l = data.split("\n")
    l = [replace_all(strings) for strings in l]

    return part1("\n".join(l))


def main():
    print(part2("oneight"))
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
