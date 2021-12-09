
def main():
    test = False
    if test:
        with open('test.txt', 'r') as f:
            strlines = f.readlines()
    else:   
        with open('input.txt', 'r') as f:
            strlines = f.readlines()

    xlines = [line.strip() for line in strlines]
    heights = [[int(c) for c in line] for line in xlines]
    heights = [[9] + line + [9] for line in heights]
    buf = [9] * len(heights[0])
    heights = [buf] + heights + [buf]

    # Part 1
    risk = 0
    basins = []
    for x in range(len(heights[0])):
        for y in range(len(heights)):
            if heights[y][x] < heights[y-1][x] and heights[y][x] < heights[y+1][x] and heights[y][x] < heights[y][x-1] and heights[y][x] < heights[y][x+1]:
                risk += heights[y][x] + 1
                basins += [(x, y)]
    print(risk)

    # Part 2
    bsizes = [basinsize(x, y, heights) for x, y in basins]
    bsizes.sort(reverse=True)
    print(bsizes[0]*bsizes[1]*bsizes[2])


def basinsize(x, y, heights):
    explored = set()
    explored.add((x, y))
    basin = explorepoint(x, y, explored, heights)
    return len(basin)

def explorepoint(x, y, explored, heights):
    bpoints = set()
    if heights[y][x] == 9:
        return bpoints

    bpoints.add((x, y))
    nextpoints = list()

    if y > 0 and heights[y][x] < heights[y-1][x] and (x, y-1) not in explored:
        nextpoints.append((x, y-1))
    if y + 1 < len(heights) and heights[y][x] < heights[y+1][x] and (x, y+1) not in explored:
        nextpoints.append((x, y+1))
    if x > 0 and heights[y][x] < heights[y][x-1] and (x-1, y) not in explored:
        nextpoints.append((x-1, y))
    if x + 1 < len(heights[0]) and heights[y][x] < heights[y][x+1] and (x+1, y) not in explored:
        nextpoints.append((x+1, y))

    nextpoints.sort(key=lambda z : height_key(z[0], z[1], heights))

    for x, y in nextpoints:
        explored.add((x, y))
        bpoints |= explorepoint(x, y, explored, heights)

    return bpoints
    return bpoints

def height_key(x, y, height):
    return height[y][x]
if __name__ == '__main__':
    main()