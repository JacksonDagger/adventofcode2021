def main():
    test = False
    if test:
        with open('test.txt', 'r') as f:
            strlines = f.readlines()
    else:   
        with open('input.txt', 'r') as f:
            strlines = f.readlines()
    
    lines = []
    for line in strlines:
        line = line.split(" -> ")
        point1 = line[0].split(",")
        point2 = line[1].split(",")
        lines.append((int(point1[0]), int(point1[1]), int(point2[0]), int(point2[1])))

    hlines = list(filter(lambda x: x[1] == x[3], lines))
    vlines = list(filter(lambda x: x[0] == x[2], lines))
    #dlines = list(filter(lambda x: abs(x[0] - x[2]) == abs(x[1] - x[3]), lines))
    dlines = list(filter(lambda x: x not in hlines and x not in vlines, lines))

    xmax = max(map(lambda x: max(x[0], x[2]), lines))
    ymax = max(map(lambda x: max(x[1], x[3]), lines))

    points = [[0] * (xmax + 1) for i in range(ymax + 1)]

    for line in hlines:
        start = min(line[0], line[2])
        end =  max(line[0], line[2])+1
        for x in range(start, end):
            points[line[1]][x] += 1
    
    for line in vlines:
        start = min(line[1], line[3])
        end =  max(line[1], line[3])+1
        for y in range(start, end):
            points[y][line[0]] += 1
    
    for line in dlines:
        if line[0] < line[2]:
            xinc = 1
        else:
            xinc = -1
        if line[1] < line[3]:
            yinc = 1
        else:
            yinc = -1
        for x, y in zip(range(line[0], line[2] + xinc, xinc), range(line[1], line[3] + yinc, yinc)):
            points[y][x] += 1

    #print(points)

    sum = 0

    for horz in points:
        for point in horz:
            if point > 1:
                sum += 1
    print(sum)

    for line in points:
        #print(line)
        pass

if __name__ == '__main__':
    main()