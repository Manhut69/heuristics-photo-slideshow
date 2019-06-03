import os
import random


def pyramid_function(min, max, mean, height):
    slope_up = (height) / (mean - min - 1)
    start_up = -(slope_up * (min - 1))

    slope_down = (-height) / (1 + max - mean)
    start_down = -(slope_down * (max + 1))

    pyramid_heights = []
    for i in range(min, max + 1):
        if i < mean:
            pyramid_heights.append(int(slope_up * i + start_up))
        else:
            pyramid_heights.append(int(slope_down * i + start_down))
    for i in range(1, len(pyramid_heights[1:]) + 1):
        pyramid_heights[i] = pyramid_heights[i] + pyramid_heights[i - 1]
    return(pyramid_heights)


def pyramid_chance(min, max, pyramid_heights):
    position = 0
    pick = random.randint(0, pyramid_heights[-1])
    while pyramid_heights[position] < pick:
        position += 1
    return(position)


if __name__ == '__main__':
    num_photos = '120'
    while not num_photos.isdigit():
        num_photos = input("Input number of lines> ")
    num_photos = int(num_photos)

    filename = 'daans_vakantiefotos_medium'
    while not os.path.isfile(f"{filename}.in"):
        filename = input("Please input the name of the .in file> ")
        if not os.path.isfile(f"{filename}.in"):
            print("File not found...")

    file = open(f"{filename}.in", 'r').readlines()

    percentage_horizontal = int(file[0])

    pyramid = file[1].split()
    min_tags = int(pyramid[0])
    max_tags = int(pyramid[1])
    mean_tags = int(pyramid[2])
    mean_height = int(pyramid[3])
    pyramid_heights = pyramid_function(min_tags, max_tags,
                                       mean_tags, mean_height)

    tags = []
    for tag_list in file[2:]:
        tags.append(tag_list.split())

    outfile = open(f"{filename}.txt", 'w')
    outfile.write(str(num_photos))
    outfile.write("\n")
    percentage_horizontal = percentage_horizontal / 100

    for i in range(num_photos):
        num_tags = min_tags + pyramid_chance(min_tags, max_tags,
                                             pyramid_heights)
        line = []
        for special_tags in tags[:-1]:
            line.append(random.choice(special_tags))

        tries = 0
        max_tries = 20
        while len(line) < num_tags and tries < max_tries:
            pick_tag = random.choice(tags[-1])
            if pick_tag not in line:
                line.append(pick_tag)
                tries = 0
            else:
                tries += 1
        num_tags = len(line)
        writeline = " ".join(line)

        random_num = random.random()
        print(f"{percentage_horizontal} > {random_num}", end=" ")
        horizontal_true = (percentage_horizontal > random.random())

        print(horizontal_true, end=" ")
        if horizontal_true:
            outfile.write(f"H {num_tags} {writeline}")
            print("H")
        else:
            outfile.write(f"V {num_tags} {writeline}")
            print("V")

        outfile.write("\n")
