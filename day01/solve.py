from aocd import get_data, submit
import re

YEAR = 2023


def del_mid_num(num):
    l = len(str(num))
    s = l - 1
    x = str(num)
    newstr = x[:1] + x[s:]
    return newstr


def part1(data):
    l = data.split("\n")
    new = []
    for item in l:
        new.append(int("".join(i for i in item if i.isdigit())))
    list = []
    for i in new:
        if i <= 9:
            list.append(i * 11)
        elif 10 <= i < 100:
            list.append(i)
        else:
            b = del_mid_num(i)
            list.append(int(b))
    print(sum(list))

    return sum(list)


dic_num = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "oneight": 18,
    "eightwo": 82,
    "threeight": 38,
    "fiveight": 58,
    "sevenine": 79,
    "nineight": 98,
}


def replace_all(text, dic):
    for i, j in dict.items(dic):
        text = text.replace(i, str(j))
    return text


def part2(data):
    l = data.split("\n")

    l = [replace_all(strings, dic_num) for strings in l]

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
