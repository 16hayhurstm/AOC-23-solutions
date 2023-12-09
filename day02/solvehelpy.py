index_red = i.find("red")
        index_numred = index_red - 2
        num_red = int(i[index_numred])
        if num_red >= 12:
            total_of_IDs += int(ID_num)
        index_blue = i.find("blue")
        index_numblue = index_blue - 2
        num_blue = int(i[index_numblue])
        if num_blue >= 14:
            total_of_IDs += int(ID_num)
        index_green = i.find("green")
        index_numgreen = index_green - 2
        num_green = int(i[index_numgreen])
        if num_green >= 13:
            total_of_IDs += int(ID_num)
        print(total_of_IDs)