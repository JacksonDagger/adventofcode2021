def main():
    test = False
    if test:
        with open('test.txt', 'r') as f:
            strlines = f.readlines()
    else:   
        with open('input.txt', 'r') as f:
            strlines = f.readlines()

    fish = strlines[0].split(',')

    for i in range(len(fish)):
        fish[i] = int(fish[i])

    fish_dict = {}
    for i in range(9):
        fish_dict[i] = fish.count(i)

    for i in range(80):
        fish = fish_day(fish)

    print(len(fish))

    for i in range(256):
        fish_dict = dict_fish_day(fish_dict)

    num_fish = 0
    for i in range(9):
        num_fish += fish_dict[i]
    print(num_fish)

def fish_day(fish):
    for i in range(len(fish)):
        if fish[i] == 0:
            fish[i] = 6
            fish.append(8)
        else:
            fish[i] -= 1
    return fish

def dict_fish_day(fish_dict):
    new_dict = {}
    for i in range(8):
        new_dict[i] = fish_dict[i + 1]
    new_dict[8] = fish_dict[0]
    new_dict[6] += fish_dict[0]
    return new_dict

if __name__ == '__main__':
    main()