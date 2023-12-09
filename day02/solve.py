from aocd import get_data, submit

YEAR = 2023


def part1(data):
    l = data.split("\n")
    suc_ID = 0
    for i in l:
        index_ID_def = i.find(":") - 3
        index_ID_may1 = index_ID_def + 1
        index_ID_may2 = index_ID_def + 2
        if index_ID_def == 5:
            ID_num = 100
        elif index_ID_may1 == 5:
            ID_num = i[index_ID_may1] + i[index_ID_may2]
        else:
            ID_num = i[index_ID_may2]
        for color, number in [("red", 12), ("blue", 14), ("green", 13)]:
            index_color = i.find(color)
            num_color_list = []
            while True:
                index_numcolor_digits = index_color - 2
                index_numcolor_tens = index_numcolor_digits - 1
                num_color = int(i[index_numcolor_tens] + i[index_numcolor_digits])
                num_color_list.append(num_color)
                ofset = index_color + 1
                index_color = i[ofset:].find(color)
                if index_color == -1:
                    break
                index_color += ofset
            if max(num_color_list) > number:
                break
        else:
            suc_ID += int(ID_num)
    return None


def part2(data):
    l = data.split("\n")
    sum_power_games = 0
    for game in l:
        power_game = 0
        print(game)
        print(sum_power_games)
        num_red_list = []
        num_blue_list = []
        num_green_list = []
        for color in ["red", "blue", "green"]:
            index_color = game.find(color)
            while True:
                index_numcolor_digits = index_color - 2
                index_numcolor_tens = index_numcolor_digits - 1
                num_color = game[index_numcolor_tens] + game[index_numcolor_digits]
                if color == "red":
                    num_red_list.append(int(num_color))
                elif color == "green":
                    num_green_list.append(int(num_color))
                elif color == "blue":
                    num_blue_list.append(int(num_color))
                print(num_red_list, num_blue_list, num_green_list)
                ofset = index_color + 1
                index_color = game[ofset:].find(color)
                if index_color == -1:
                    break
                index_color += ofset
        power_game = max(num_blue_list) * max(num_green_list) * max(num_red_list)
        print(power_game)
        sum_power_games += power_game
        print(sum_power_games)
    return sum_power_games


data_test = [
    "Game 1: 1 red, 1 blue, 11 green; 6 blue, 2 red, 14 green; 3 green, 2 red; 9 blue, 10 green",
    "Game 2: 6 green, 4 blue, 15 red; 13 red, 7 blue, 3 green; 14 red, 5 blue, 6 green; 5 blue, 7 red, 2 green",
    "Game 3: 4 blue, 2 red; 6 green, 6 blue, 4 red; 8 green, 1 blue, 3 red",
]


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
